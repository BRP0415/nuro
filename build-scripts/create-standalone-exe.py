#!/usr/bin/env python3
"""
Simple Nuro .exe builder
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_cmd(cmd):
    """Run command"""
    print(f"\n>>> {cmd}\n")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"\n❌ Command failed!")
        sys.exit(1)

root = Path(__file__).parent.parent
os.chdir(root)

print("\n" + "="*60)
print("🚀 Building Nuro Standalone .EXE")
print("="*60)

print("\n[1/3] Building React frontend...")
run_cmd("npm run build")

print("\n[2/3] Creating bundle directory...")
bundle_dir = root / "bundle"
if bundle_dir.exists():
    shutil.rmtree(bundle_dir)
bundle_dir.mkdir()

print("\n[3/3] Copying files...")
react_build = root / "build"
if react_build.exists():
    shutil.copytree(react_build, bundle_dir / "frontend", dirs_exist_ok=True)

backend_src = root / "backend"
shutil.copytree(backend_src, bundle_dir / "backend", dirs_exist_ok=True)

print("\n" + "="*60)
print("✅ Build files ready in: bundle/")
print("="*60)
print(f"\n📦 Frontend: {bundle_dir / 'frontend'}")
print(f"⚙️  Backend: {bundle_dir / 'backend'}")
print(f"\n💾 Files bundled and ready!")
print("="*60 + "\n")
