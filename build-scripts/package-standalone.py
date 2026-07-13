#!/usr/bin/env python3
"""
Package Nuro as a complete standalone executable with NSI installer.
Uses NSIS to create professional Windows installer.
"""

import os
import sys
import shutil
from pathlib import Path
import subprocess

def create_nsis_installer():
    """Create NSIS installer script"""
    nsis_script = '''!include "MUI2.nsh"
!include "x64.nsh"

; General
Name "Nuro"
OutFile "Nuro-Setup.exe"
InstallDir "$PROGRAMFILES\\Nuro"
InstallDirRegKey HKLM "Software\\Nuro" "Install_Dir"

; MUI Settings
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_LANGUAGE "English"

; Installer sections
Section "Install"
  SetOutPath "$INSTDIR"
  File "dist\\Nuro.exe"
  CreateDirectory "$SMPROGRAMS\\Nuro"
  CreateShortCut "$SMPROGRAMS\\Nuro\\Nuro.lnk" "$INSTDIR\\Nuro.exe"
  CreateShortCut "$DESKTOP\\Nuro.lnk" "$INSTDIR\\Nuro.exe"
  WriteRegStr HKLM "Software\\Nuro" "Install_Dir" "$INSTDIR"
SectionEnd

Section "Uninstall"
  RMDir /r "$INSTDIR"
  RMDir /r "$SMPROGRAMS\\Nuro"
  Delete "$DESKTOP\\Nuro.lnk"
  DeleteRegKey HKLM "Software\\Nuro"
SectionEnd
'''
    return nsis_script

def build():
    print("\n" + "="*60)
    print("📦 Packaging Nuro Standalone Installer")
    print("="*60)
    
    root = Path(__file__).parent.parent
    bundle = root / "bundle"
    
    print(f"\n✅ Bundle ready at {bundle / 'dist' / 'Nuro.exe'}")
    print("\nNow creating installer with NSIS...")
    
    # Create NSIS script
    nsis_file = bundle / "nuro.nsi"
    nsis_file.write_text(create_nsis_installer())
    
    # Compile with NSIS if available
    try:
        subprocess.run(["makensis", str(nsis_file)], check=True)
        print(f"\n✅ Installer created: {bundle / 'Nuro-Setup.exe'}")
    except FileNotFoundError:
        print("\n⚠️  NSIS not found. Skipping installer creation.")
        print(f"\nYour standalone .exe is ready at: {bundle / 'dist' / 'Nuro.exe'}")
        print("You can distribute this directly without installation!")

if __name__ == "__main__":
    build()
