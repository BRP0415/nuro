# ✨ Nuro - Standalone AI Assistant

**Download. Run. No Installation. No Prerequisites.**

A beautiful, fully self-contained AI assistant that runs entirely on your machine with computer control, brain visualization, and advanced coding knowledge.

## 🚀 Quick Start

1. **[Download Nuro-Standalone.exe](https://github.com/BRP0415/nuro/releases)**
2. **Double-click to run**
3. **Chat with your AI** ✨

That's it!

## ✨ Features

- 💬 **Beautiful Chat Interface** - Jarvis-style conversation
- 🧠 **Brain Visualization** - Watch the AI think in real-time
- 🖥️ **Computer Control** - Safe, approved mouse/keyboard automation
- 💻 **Expert Coding** - Advanced programming knowledge and assistance
- 📚 **General Knowledge** - Answer questions, explain concepts
- 🔒 **100% Private** - Everything runs locally, no cloud uploads
- ⚡ **Fast** - Instant responses with smart model
- 🎨 **Beautiful UI** - Modern, responsive design

## 🎯 Use Cases

- 💡 **Get coding help** - Debug, refactor, optimize code
- 🤔 **Ask questions** - Get detailed explanations
- 🔧 **Automate tasks** - Control your computer safely
- 📊 **Analyze data** - Parse and understand information
- 🎓 **Learn** - Educational explanations and examples

## 📋 System Requirements

- Windows 10+ (64-bit)
- 8GB RAM (16GB+ recommended)
- 15GB disk space
- Internet (first run to download model)

## 💾 What's Included

The `.exe` contains:
- ✅ Python runtime
- ✅ FastAPI backend
- ✅ React frontend
- ✅ Electron app shell
- ✅ Ollama integration

## 🎮 How to Use

### Chat

Just type questions and chat naturally:
- "How do I implement authentication in React?"
- "Explain quantum computing"
- "What's the capital of France?"
- "Help me debug this code"

### View Brain

Click the "Brain" tab to see:
- Neural network activation
- Thinking process visualization
- Real-time statistics
- Token generation rate

### Control

Click the "Control" tab to:
- Enable/disable AI control
- Set permissions
- View system status
- Check privacy info

## 🔐 Privacy & Security

✅ **All processing happens locally**  
✅ **No data sent to servers**  
✅ **No API keys required**  
✅ **No account needed**  
✅ **You control permissions**  
✅ **Can be used offline**  

## ⚙️ Customization

Change AI model by editing:

```
C:\Users\YourName\.nuro\config.json
```

Available models:
- `mistral` - Fast, good all-around (default)
- `llama2` - Larger, more capable
- `deepseek-coder` - Best for coding
- `neural-chat` - Optimized for conversation

## 🐛 Troubleshooting

**"Ollama not found"**
- Install from https://ollama.ai/
- Nuro will guide you

**"Taking too long to start"**
- First run downloads the AI model (~4GB)
- Subsequent runs are instant

**"Port already in use"**
- Close other applications using ports 8000 or 11434
- Or restart your computer

See [STANDALONE.md](STANDALONE.md) for full troubleshooting guide.

## 📦 Building from Source

```bash
# Install dependencies
npm install
pip install -r backend/requirements.txt

# Build standalone .exe
npm run build:exe

# Creates: dist/Nuro.exe (~500MB)
```

## 📄 License

MIT

## 🙏 Credits

- Powered by [Ollama](https://ollama.ai/) for local LLMs
- Built with [Electron](https://electronjs.org/) and [React](https://react.dev/)
- Backend using [FastAPI](https://fastapi.tiangolo.com/)

## 🚀 What's Next?

- Try asking about your favorite programming language
- Enable computer control and automate a task
- Customize the system prompt for specific use cases
- Experiment with different AI models

---

**Made with ❤️ as a local AI assistant**

[Download Now](https://github.com/BRP0415/nuro/releases) | [View Source](https://github.com/BRP0415/nuro) | [Report Issues](https://github.com/BRP0415/nuro/issues)
