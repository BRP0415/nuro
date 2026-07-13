# 🚀 Nuro Standalone .EXE

## What You Get

A **single .exe file** that contains:
- ✅ Python runtime
- ✅ Node.js runtime (via Electron)
- ✅ React frontend
- ✅ FastAPI backend
- ✅ Ollama launcher
- ✅ Everything needed to run

**No installation. No prerequisites. Just run it.**

---

## Installation

### Option 1: Completely Standalone (Recommended)

1. **Download** `Nuro-Standalone.exe`
2. **Double-click** to run
3. **Done!** ✨

That's it. The exe will:
- Check for Ollama
- Download the AI model (first time only, ~4GB)
- Start the backend
- Open your browser

### Option 2: With Ollama Pre-installed

If you already have [Ollama](https://ollama.ai/) installed:
1. Run `ollama serve` in a terminal (keep it open)
2. Download and run `Nuro.exe`
3. Done!

---

## How It Works

### First Run

```
✨ Nuro Initializing...
🧠 Starting Ollama...
⏳ Waiting for Ollama to start...
✅ Ollama ready
🤖 Checking for mistral model...
📥 Downloading model (may take 5-10 mins)...
✅ mistral model ready
⚙️  Starting Nuro backend...
✅ Backend ready
✅ Nuro is ready!
🎨 Opening interface...
```

Then your browser opens with Nuro's chat interface.

### Subsequent Runs

```
✨ Nuro Initializing...
✅ Ollama already running
✅ mistral model ready
✅ Backend ready
✅ Nuro is ready!
🎨 Opening interface...
```

Everything starts in seconds.

---

## System Requirements

- **Windows 10+** (64-bit)
- **8GB RAM minimum** (16GB+ recommended for better performance)
- **~15GB disk space** for:
  - Nuro executable: ~300MB
  - Ollama: ~500MB
  - Model (mistral): ~4GB
  - Cache/temp: ~1GB
- **GPU optional** (NVIDIA CUDA for faster responses)

---

## Features

### 💬 Chat Interface
- Ask questions
- Get coding help
- Get explanations
- Multi-turn conversations

### 🧠 Brain Visualization
- Watch the AI think
- See neural network activation
- Token generation rate
- Real-time statistics

### 🖥️ Computer Control
- Safe mouse/keyboard control
- Screenshot capability
- All with your approval
- Toggle on/off anytime

### 🔒 Privacy
- Everything runs locally
- No cloud uploads
- No account needed
- No API keys

---

## Customization

### Change the AI Model

Edit the config file (once Nuro creates it):

```
C:\Users\YourName\.nuro\config.json
```

Change `model_name`:
- `mistral` - Fast, good coding (default)
- `llama2` - Larger, smarter
- `neural-chat` - Great for chat
- `deepseek-coder` - Best for coding

Then restart Nuro.

### Disable Startup Download

Pre-download the model:

```bash
ollama pull mistral
```

Then Nuro won't need to download it.

---

## Troubleshooting

### "Ollama not found"

**Solution**: Install Ollama from https://ollama.ai/

Nuro will still work - it just can't auto-start Ollama.

### Takes a long time on first run

That's normal! The AI model is ~4GB and downloads from the internet.

### Port 8000 or 11434 already in use

Another application is using these ports. Either:
- Close the other app
- Or restart your computer

### "Nuro is slow"

That means you need:
- More RAM (8GB minimum, 16GB+ better)
- GPU (NVIDIA preferred)
- Or use a smaller model:
  ```bash
  ollama pull neural-chat
  ```

---

## Advanced Usage

### Launch with Custom Model

Create a batch file (`launch-nuro.bat`):

```batch
@echo off
set NURO_MODEL=deepseek-coder
Nuro.exe
```

### Use from Command Line

Check backend health:

```bash
curl http://localhost:8000/api/health
```

Take screenshot:

```bash
curl -X POST http://localhost:8000/api/control/screenshot
```

---

## Uninstall

1. Delete `Nuro.exe`
2. Delete `C:\Users\YourName\.nuro` folder (optional, frees ~5GB)

That's it. No registry changes, no leftover files.

---

## Support

For issues:
1. Check troubleshooting above
2. Visit: https://github.com/BRP0415/nuro/issues
3. Report the error message you see

---

## What's Next?

- 🎯 Try asking for coding help
- 🖥️ Enable computer control and try automation
- 👀 Watch the brain visualization
- 🔧 Customize the AI with different models

**Enjoy your local AI assistant!** ✨
