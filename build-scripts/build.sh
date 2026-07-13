#!/bin/bash

echo "============================================"
echo "Building Nuro .EXE Installer"
echo "============================================"

# Step 1: Build React app
echo ""
echo "[1/4] Building React frontend..."
npm run build
if [ $? -ne 0 ]; then
    echo "Failed to build React app"
    exit 1
fi

# Step 2: Build Python backend exe
echo ""
echo "[2/4] Building Python backend..."
cd backend
pyinstaller --onefile --windowed --name nuro_backend nuro_backend.py
if [ $? -ne 0 ]; then
    echo "Failed to build Python backend"
    exit 1
fi
cd ..

# Step 3: Install dependencies
echo ""
echo "[3/4] Installing dependencies..."
npm install
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies"
    exit 1
fi

# Step 4: Build Electron app
echo ""
echo "[4/4] Building Electron installer..."
npm run build:exe
if [ $? -ne 0 ]; then
    echo "Failed to build Electron installer"
    exit 1
fi

echo ""
echo "============================================"
echo "✓ Build complete!"
echo "Find your installer in the 'dist' folder"
echo "============================================"
