# ✨ Nuro - AI Assistant with Computer Control

A beautiful, locally-running AI assistant with desktop control, coding knowledge, and real-time brain visualization. No API keys required.

## Features

- 🧠 **Beautiful Brain Visualization**: Real-time neural network activity visualization
- 💻 **Computer Control**: Safe, user-approved mouse/keyboard control
- 🤖 **Local LLM**: Runs entirely on your machine (Llama 3, Mistral, DeepSeek)
- 💬 **Chat Interface**: Jarvis-like conversational AI
- 📦 **Single .EXE**: Download, run, done. No installation needed.

## Quick Start

1. Download `Nuro-Setup.exe` from [Releases](https://github.com/BRP0415/nuro/releases)
2. Run the installer
3. Launch Nuro from your desktop
4. Chat with your AI assistant!

## System Requirements

- Windows 10+
- 8GB RAM (16GB+ recommended)
- ~5GB disk space (for bundled model)
- GPU optional (faster responses with NVIDIA CUDA)

## Building from Source

```bash
# Clone repo
git clone https://github.com/BRP0415/nuro.git
cd nuro

# Install dependencies
npm install
pip install -r backend/requirements.txt

# Build .exe
npm run build:exe
```

## Project Structure

```
nuro/
├── frontend/                # React + 3D visualization
├── backend/                 # Python FastAPI server
├── electron/                # Electron main process
├── build-scripts/           # Packaging & .exe generation
└── config/                  # Configuration files
```

## Architecture

- **Frontend**: React + Three.js for 3D brain visualization
- **Backend**: Python FastAPI with local Ollama integration
- **Desktop**: Electron for cross-platform native experience
- **Package**: PyInstaller bundles Python; electron-builder creates .exe

## License

MIT
