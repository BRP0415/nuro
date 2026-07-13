@echo off
echo ============================================
echo Building Nuro .EXE Installer
echo ============================================

REM Step 1: Build React app
echo.
echo [1/4] Building React frontend...
call npm run build
if errorlevel 1 (
    echo Failed to build React app
    exit /b 1
)

REM Step 2: Build Python backend exe
echo.
echo [2/4] Building Python backend...
cd backend
pyinstaller --onefile --windowed --name nuro_backend nuro_backend.py
if errorlevel 1 (
    echo Failed to build Python backend
    exit /b 1
)
cd ..

REM Step 3: Install electron-builder dependencies
echo.
echo [3/4] Installing Electron dependencies...
call npm install
if errorlevel 1 (
    echo Failed to install dependencies
    exit /b 1
)

REM Step 4: Build Electron app
echo.
echo [4/4] Building Electron installer...
call npm run build:exe
if errorlevel 1 (
    echo Failed to build Electron installer
    exit /b 1
)

echo.
echo ============================================
echo ✓ Build complete!
echo Find your installer in the 'dist' folder
echo ============================================
pause
