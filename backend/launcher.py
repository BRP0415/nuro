#!/usr/bin/env python3
"""
Nuro Backend Launcher
Handles Ollama startup and model initialization
"""

import os
import sys
import subprocess
import time
import json
import signal
import platform
from pathlib import Path
import http.client
import socket

# Configuration
OLLAMA_PORT = 11434
BACKEND_PORT = 8000
DEFAULT_MODEL = "mistral"
MAX_RETRIES = 30
RETRY_DELAY = 1

class NuroLauncher:
    def __init__(self):
        self.app_dir = Path(__file__).parent.parent
        self.home_dir = Path.home()
        self.cache_dir = self.home_dir / ".nuro"
        self.models_dir = self.cache_dir / "models"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.models_dir.mkdir(parents=True, exist_ok=True)
        self.ollama_process = None
        self.backend_process = None

    def is_port_in_use(self, port):
        """Check if port is already in use"""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0

    def wait_for_service(self, port, max_attempts=MAX_RETRIES):
        """Wait for a service to be ready on a port"""
        for attempt in range(max_attempts):
            if self.is_port_in_use(port):
                return True
            time.sleep(RETRY_DELAY)
        return False

    def start_ollama(self):
        """Start Ollama service"""
        if self.is_port_in_use(OLLAMA_PORT):
            print(f"✅ Ollama already running on port {OLLAMA_PORT}")
            return True

        print(f"🧠 Starting Ollama...")
        
        try:
            if platform.system() == "Windows":
                # Windows: Look for ollama in PATH or default location
                ollama_exe = "ollama"
                try:
                    # Try to find Ollama installation
                    result = subprocess.run(["where", "ollama"], capture_output=True, text=True)
                    if result.returncode == 0:
                        ollama_exe = result.stdout.strip()
                except:
                    pass
            else:
                ollama_exe = "ollama"

            self.ollama_process = subprocess.Popen(
                [ollama_exe, "serve"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True  # Detach process
            )
            
            print(f"⏳ Waiting for Ollama to start...")
            if self.wait_for_service(OLLAMA_PORT):
                print(f"✅ Ollama ready on port {OLLAMA_PORT}")
                return True
            else:
                print(f"❌ Ollama failed to start")
                return False
                
        except FileNotFoundError:
            print(f"\n❌ Ollama not found!")
            print(f"\n📥 Please install Ollama:")
            print(f"   Windows: https://ollama.ai/download/windows")
            print(f"   macOS: https://ollama.ai/download/mac")
            print(f"   Linux: https://ollama.ai/download/linux")
            return False
        except Exception as e:
            print(f"❌ Failed to start Ollama: {e}")
            return False

    def ensure_model(self):
        """Ensure model is downloaded"""
        print(f"🤖 Checking for {DEFAULT_MODEL} model...")
        
        try:
            # Try to pull model
            result = subprocess.run(
                ["ollama", "pull", DEFAULT_MODEL],
                capture_output=True,
                text=True,
                timeout=600  # 10 min timeout
            )
            
            if result.returncode == 0:
                print(f"✅ {DEFAULT_MODEL} model ready")
                return True
            else:
                print(f"❌ Failed to pull {DEFAULT_MODEL}")
                print(result.stderr)
                return False
        except subprocess.TimeoutExpired:
            print(f"⏱️  Model download taking too long...")
            return False
        except Exception as e:
            print(f"❌ Error checking model: {e}")
            return False

    def start_backend(self):
        """Start FastAPI backend"""
        print(f"\n⚙️  Starting Nuro backend...")
        
        backend_script = self.app_dir / "backend" / "nuro_backend.py"
        
        try:
            self.backend_process = subprocess.Popen(
                [sys.executable, str(backend_script)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            print(f"⏳ Waiting for backend to start...")
            if self.wait_for_service(BACKEND_PORT):
                print(f"✅ Backend ready on port {BACKEND_PORT}")
                return True
            else:
                print(f"❌ Backend failed to start")
                return False
        except Exception as e:
            print(f"❌ Failed to start backend: {e}")
            return False

    def run(self):
        """Main launcher"""
        print("\n" + "="*60)
        print("✨ Nuro Initializing...")
        print("="*60 + "\n")

        # Start Ollama
        if not self.start_ollama():
            return False

        time.sleep(2)

        # Ensure model
        if not self.ensure_model():
            print("\n⚠️  Continuing without model check...")

        # Start backend
        if not self.start_backend():
            return False

        print("\n" + "="*60)
        print("✅ Nuro is ready!")
        print("🎨 Opening interface...")
        print("="*60 + "\n")

        return True

    def cleanup(self):
        """Cleanup processes"""
        if self.ollama_process:
            try:
                self.ollama_process.terminate()
            except:
                pass
        if self.backend_process:
            try:
                self.backend_process.terminate()
            except:
                pass

if __name__ == "__main__":
    launcher = NuroLauncher()
    
    try:
        success = launcher.run()
        if not success:
            sys.exit(1)
        
        # Keep running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Shutting down...")
        launcher.cleanup()
        sys.exit(0)
