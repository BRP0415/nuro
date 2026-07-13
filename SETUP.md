# 🚀 Nuro Setup & Build Guide

## Prerequisites

### Required Software

1. **Node.js** (v16+)
   - Download: https://nodejs.org/
   - Verify: `node --version` & `npm --version`

2. **Python** (3.9+)
   - Download: https://python.org/
   - Verify: `python --version`

3. **Git** (optional, for cloning)
   - Download: https://git-scm.com/

4. **Ollama** (for local LLM)
   - Download: https://ollama.ai/
   - After install, run: `ollama serve` (keep this terminal open)

## Installation Steps

### 1. Clone/Download the Repository

```bash
git clone https://github.com/BRP0415/nuro.git
cd nuro
```

### 2. Install Dependencies

```bash
# Install Node dependencies
npm install

# Install Python dependencies
cd backend
pip install -r requirements.txt
cd ..
```

### 3. Start Ollama

Before running Nuro, you must have Ollama running:

```bash
# Open a new terminal and run:
ollama serve

# Download a model (this is automatic on first run, but you can do it manually):
ollama pull mistral
```

### 4. Run in Development Mode

```bash
# Terminal 1: Start Python backend
cd backend
python nuro_backend.py

# Terminal 2: Start React + Electron
npm start
```

The app should open automatically!

## Building the .EXE Installer

### Windows

```bash
build-scripts\build-exe.bat
```

The installer will be in `dist/` folder.

### macOS/Linux

```bash
chmod +x build-scripts/build.sh
./build-scripts/build.sh
```

## Troubleshooting

### "Ollama is not running" error
- Make sure you have Ollama installed from https://ollama.ai/
- Run `ollama serve` in a separate terminal
- Keep that terminal open while using Nuro

### Backend won't start
- Check that port 8000 is not in use: `netstat -ano | findstr :8000` (Windows)
- Make sure Python is installed: `python --version`
- Reinstall backend dependencies: `pip install -r backend/requirements.txt`

### React won't compile
- Delete `node_modules/` and `package-lock.json`
- Run `npm install` again
- Try `npm start`

### Build fails
- Make sure you have Administrator access
- Check that all prerequisites are installed
- Try building each component separately first

## Project Structure

```
nuro/
├── src/                    # React frontend
├── electron/               # Electron main process
├── backend/                # Python FastAPI server
├── build-scripts/          # Build automation
├── public/                 # Static assets
└── package.json            # Node dependencies
```

## Advanced Configuration

### Change LLM Model

Edit `backend/nuro_backend.py` line 19:

```python
MODEL_NAME = "llama2"  # or "neural-chat", "mistral", etc.
```

Then install the model:

```bash
ollama pull llama2
```

### System Prompts

Edit the system prompt in `backend/nuro_backend.py` in the `NuroBrain` class to customize Nuro's behavior.

## Performance Tips

- Use GPU acceleration: Install NVIDIA CUDA for faster inference
- Smaller models run faster: `phi`, `mistral`, `neural-chat` are quick
- Larger models are smarter: `llama2-13b`, `mistral-large` are better
- 16GB+ RAM recommended for smooth operation

## Security Notes

- ✅ All processing happens locally
- ✅ No data sent to external servers
- ✅ You control all permissions
- ✅ Disable AI control anytime
- ✅ No credentials or sensitive data stored

## Support

For issues:
1. Check this guide
2. Review error messages carefully
3. Open a GitHub issue

Happy coding! 🚀
