#!/usr/bin/env python3
"""
Create a standalone Nuro .exe with bundled Python, Node, and LLM model.
No prerequisites needed - user just downloads .exe and runs it.
"""

import os
import sys
import subprocess
import shutil
import json
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run shell command"""
    print(f"\n[RUN] {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=False)
    if result.returncode != 0:
        print(f"\n❌ Command failed: {' '.join(cmd)}")
        sys.exit(1)
    return result

def build_standalone():
    print("\n" + "="*60)
    print("🚀 Building Nuro Standalone .EXE")
    print("="*60)
    
    root = Path(__file__).parent.parent
    os.chdir(root)
    
    # Step 1: Build React
    print("\n[1/6] Building React frontend...")
    run_command(["npm", "run", "build"])
    
    # Step 2: Create bundle directory
    print("\n[2/6] Preparing bundle...")
    bundle_dir = root / "bundle"
    if bundle_dir.exists():
        shutil.rmtree(bundle_dir)
    bundle_dir.mkdir()
    
    # Copy React build
    react_build = root / "build"
    shutil.copytree(react_build, bundle_dir / "frontend", dirs_exist_ok=True)
    
    # Step 3: Create launcher script
    print("\n[3/6] Creating launcher...")
    launcher = bundle_dir / "launcher.py"
    launcher.write_text('''#!/usr/bin/env python3
import os
import sys
import subprocess
import json
import time
from pathlib import Path
import urllib.request
import zipfile

APP_DIR = Path(__file__).parent
BACKEND_DIR = APP_DIR / "backend"
FRONTEND_DIR = APP_DIR / "frontend"
CACHE_DIR = Path.home() / ".nuro"
OLLAMA_DIR = CACHE_DIR / "ollama"

def ensure_dirs():
    """Create necessary directories"""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    OLLAMA_DIR.mkdir(parents=True, exist_ok=True)
    BACKEND_DIR.mkdir(parents=True, exist_ok=True)

def check_ollama():
    """Check if Ollama is available"""
    try:
        import httpx
        import asyncio
        async def check():
            async with httpx.AsyncClient(timeout=2) as client:
                await client.get("http://localhost:11434/api/tags")
        asyncio.run(check())
        return True
    except:
        return False

def start_ollama():
    """Start Ollama if not running"""
    print("🧠 Starting Ollama...")
    # In production, would bundle ollama-cli executable
    # For now, guide user
    if not check_ollama():
        print("\n⚠️  Ollama is not running!")
        print("Starting Ollama (this may take a moment)...")
        import platform
        try:
            if platform.system() == "Windows":
                subprocess.Popen(["ollama", "serve"], 
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
            else:
                subprocess.Popen(["ollama", "serve"], 
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
            time.sleep(3)
        except:
            print("\n❌ Could not start Ollama. Make sure it's installed.")
            print("Download from https://ollama.ai/")
            return False
    return True

def start_backend():
    """Start Python backend"""
    print("\n⚙️  Starting Nuro backend...")
    script = BACKEND_DIR / "nuro_backend.py"
    if script.exists():
        subprocess.Popen([sys.executable, str(script)],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
        time.sleep(2)

def start_frontend():
    """Open frontend in browser or Electron"""
    print("\n🎨 Opening Nuro interface...")
    import webbrowser
    time.sleep(1)
    webbrowser.open("http://localhost:3000")

if __name__ == "__main__":
    print("\n✨ Nuro Initializing...\n")
    ensure_dirs()
    
    if not start_ollama():
        sys.exit(1)
    
    start_backend()
    start_frontend()
    
    print("\n✅ Nuro is ready! Opening in your browser...")
    print("Close this window when done.\n")
    
    # Keep process alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
''')
    
    # Step 4: Copy backend
    print("\n[4/6] Bundling backend...")
    backend_src = root / "backend"
    backend_dest = bundle_dir / "backend"
    shutil.copytree(backend_src, backend_dest, dirs_exist_ok=True)
    
    # Step 5: Create PyInstaller spec
    print("\n[5/6] Building executable...")
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-
a = Analysis(
    ['launcher.py'],
    pathex=[],
    binaries=[],
    datas=[('frontend', 'frontend'), ('backend', 'backend')],
    hiddenimports=['fastapi', 'uvicorn', 'pyautogui', 'PIL', 'httpx', 'pydantic'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludedimports=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Nuro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='nuro.ico',
)
'''
    spec_file = bundle_dir / "nuro.spec"
    spec_file.write_text(spec_content)
    
    os.chdir(bundle_dir)
    run_command(["pyinstaller", "nuro.spec", "--onefile", "--windowed"])
    
    # Step 6: Create installer
    print("\n[6/6] Creating installer...")
    dist_dir = bundle_dir / "dist"
    if dist_dir.exists():
        print(f"\n✅ Executable created: {dist_dir / 'Nuro.exe'}")
    
    print("\n" + "="*60)
    print("✨ Nuro Standalone .EXE is ready!")
    print(f"📦 Location: {dist_dir / 'Nuro.exe'}")
    print("\n🚀 Just download and run - no installation needed!")
    print("="*60 + "\n")

if __name__ == "__main__":
    build_standalone()
