import asyncio
import json
import os
import sys
from pathlib import Path
import httpx
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import pyautogui
from PIL import ImageGrab
import base64
import io

app = FastAPI(title="Nuro Backend")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_BASE = "http://localhost:11434"
MODEL_NAME = "mistral"  # You can change to llama2, neural-chat, etc.


class NuroBrain:
    def __init__(self):
        self.conversation_history = []
        self.system_prompt = """You are Nuro, an advanced local AI assistant running entirely on the user's machine.

Your personality:
- You are helpful, intelligent, and thoughtful
- You think step-by-step before responding
- You can see the user's screen and understand context
- You have strong coding knowledge in Python, JavaScript, React, and other languages
- You explain complex concepts clearly

Capabilities:
- Computer control (mouse, keyboard, screenshots)
- File system operations
- Task automation
- Coding assistance
- General knowledge and reasoning

When helping with actions:
1. Explain what you'll do in clear terms
2. Ask for confirmation before significant actions
3. Perform the action
4. Report results and next steps

Always prioritize the user's safety and privacy. Never perform destructive actions without explicit confirmation."""

    async def think(self, user_message: str):
        """Stream thinking process to frontend"""
        self.conversation_history.append({"role": "user", "content": user_message})

        # Check if Ollama is running
        try:
            async with httpx.AsyncClient(timeout=5) as client:
                await client.get(f"{OLLAMA_BASE}/api/tags")
        except httpx.ConnectError:
            yield json.dumps({
                "type": "error",
                "error": "Ollama is not running. Please install Ollama from https://ollama.ai and run 'ollama serve' in a terminal."
            })
            return

        try:
            async with httpx.AsyncClient(timeout=None) as client:
                async with client.stream(
                    "POST",
                    f"{OLLAMA_BASE}/api/generate",
                    json={
                        "model": MODEL_NAME,
                        "prompt": self._build_prompt(user_message),
                        "stream": True,
                        "temperature": 0.7,
                        "top_p": 0.9,
                    },
                ) as response:
                    full_response = ""
                    async for line in response.aiter_lines():
                        if line:
                            try:
                                data = json.loads(line)
                                token = data.get("response", "")
                                full_response += token
                                yield json.dumps({
                                    "type": "token",
                                    "content": token,
                                    "full": full_response
                                })
                            except json.JSONDecodeError:
                                pass

            self.conversation_history.append({"role": "assistant", "content": full_response})
            yield json.dumps({"type": "done"})
        except Exception as e:
            yield json.dumps({"type": "error", "error": str(e)})

    def _build_prompt(self, user_message: str) -> str:
        """Build prompt from conversation history"""
        prompt = self.system_prompt + "\n\n"
        
        # Include last few messages for context
        for msg in self.conversation_history[-4:]:
            prompt += f"{msg['role'].upper()}: {msg['content']}\n\n"
        
        prompt += f"USER: {user_message}\n\nASSISTANT: "
        return prompt


brain = NuroBrain()


@app.websocket("/ws/chat")
async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            content = message_data.get("content", "")
            
            if content.strip():
                async for response in brain.think(content):
                    await websocket.send_text(response)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"WebSocket error: {e}")
        try:
            await websocket.send_text(json.dumps({
                "type": "error",
                "error": str(e)
            }))
        except:
            pass


@app.post("/api/control/screenshot")
async def take_screenshot():
    """Capture screenshot for AI context"""
    try:
        img = ImageGrab.grab()
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_base64 = base64.b64encode(img_bytes.getvalue()).decode()
        return {"image": img_base64, "success": True}
    except Exception as e:
        return {"error": str(e), "success": False}


@app.post("/api/control/click")
async def click(x: int, y: int):
    """Click at coordinates"""
    try:
        pyautogui.click(x, y)
        return {"success": True}
    except Exception as e:
        return {"error": str(e), "success": False}


@app.post("/api/control/type")
async def type_text(text: str):
    """Type text"""
    try:
        pyautogui.typewrite(text, interval=0.05)
        return {"success": True}
    except Exception as e:
        return {"error": str(e), "success": False}


@app.post("/api/control/move")
async def move_mouse(x: int, y: int):
    """Move mouse"""
    try:
        pyautogui.moveTo(x, y, duration=0.5)
        return {"success": True}
    except Exception as e:
        return {"error": str(e), "success": False}


@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "nuro-backend"}


if __name__ == "__main__":
    print("🤖 Nuro Backend Starting...")
    print(f"📦 Model: {MODEL_NAME}")
    print(f"🔗 Ollama: {OLLAMA_BASE}")
    print("\n⚠️  Make sure Ollama is running: 'ollama serve'")
    print("\n🚀 Server running on http://localhost:8000")
    
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
