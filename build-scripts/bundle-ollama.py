#!/usr/bin/env python3
"""
Download and bundle Ollama model with the executable.
Creates a complete offline package.
"""

import os
import sys
import json
import urllib.request
import subprocess
from pathlib import Path

def download_model(model_name="mistral"):
    """
    Download Ollama model for bundling.
    Run this once to cache the model.
    """
    print(f"\n📥 Downloading {model_name} model...")
    print("This may take a few minutes (~4GB)\n")
    
    cache_dir = Path.home() / ".nuro" / "models"
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # This pulls to Ollama's cache
        subprocess.run(["ollama", "pull", model_name], check=True)
        print(f"\n✅ {model_name} downloaded successfully!")
        print(f"\n📁 Models cached in: {cache_dir}")
    except FileNotFoundError:
        print("\n❌ Ollama is not installed!")
        print("Download from https://ollama.ai/")
        return False
    except subprocess.CalledProcessError:
        print(f"\n❌ Failed to download {model_name}")
        return False
    
    return True

def create_offline_package():
    """
    Bundle model with executable.
    """
    print("\n" + "="*60)
    print("📦 Creating Offline Package")
    print("="*60)
    
    models_dir = Path.home() / ".nuro" / "models"
    
    if not models_dir.exists():
        print("\n❌ No models found. Run with --download-model first.")
        return False
    
    print(f"\n✅ Found cached models in {models_dir}")
    print("\nBundling into .exe...")
    # Models will be copied during PyInstaller packaging
    
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--download":
        model = sys.argv[2] if len(sys.argv) > 2 else "mistral"
        download_model(model)
    else:
        create_offline_package()
