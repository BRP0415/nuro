import React, { useState, useRef, useEffect } from 'react';
import { Send, Loader, Zap } from 'lucide-react';
import { useNuroStore } from '../store/nuroStore';

const ChatInterface = () => {
  const [input, setInput] = useState('');
  const messagesEndRef = useRef(null);
  const { messages, thinking, sendMessage, connectionStatus } = useNuroStore();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = () => {
    if (input.trim() && !thinking && connectionStatus === 'connected') {
      sendMessage(input);
      setInput('');
    }
  };

  return (
    <div className="flex flex-col h-full">
      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center text-center">
            <div className="text-6xl mb-4">🤖</div>
            <h2 className="text-2xl font-bold mb-2">Welcome to Nuro</h2>
            <p className="text-gray-400 max-w-md mb-6">
              I'm your local AI assistant. I can help with coding, answer questions, and control your computer when you need me to.
            </p>
            <div className="grid grid-cols-2 gap-3 text-sm">
              {[
                { emoji: '💻', text: 'Code help' },
                { emoji: '🔧', text: 'System tasks' },
                { emoji: '📚', text: 'General knowledge' },
                { emoji: '🎯', text: 'Automation' },
              ].map((item, i) => (
                <div key={i} className="bg-gray-800/50 p-3 rounded-lg backdrop-blur">
                  <div className="text-xl mb-1">{item.emoji}</div>
                  <div className="text-xs text-gray-300">{item.text}</div>
                </div>
              ))}
            </div>
          </div>
        ) : (
          messages.map((msg, idx) => (
            <div
              key={idx}
              className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
            >
              <div
                className={`max-w-xl px-4 py-3 rounded-lg backdrop-blur-sm ${
                  msg.role === 'user'
                    ? 'bg-gradient-to-r from-blue-500 to-purple-500 text-white rounded-br-none'
                    : 'bg-gray-800/50 text-gray-100 rounded-bl-none border border-purple-500/20'
                }`}
              >
                <div className="text-sm leading-relaxed whitespace-pre-wrap">
                  {msg.content}
                  {msg.thinking && (
                    <div className="inline-block ml-2 animate-pulse">▌</div>
                  )}
                </div>
              </div>
            </div>
          ))
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Area */}
      <div className="border-t border-purple-500/20 bg-black/30 p-4 backdrop-blur-md">
        {connectionStatus !== 'connected' && (
          <div className="mb-3 p-3 bg-yellow-500/10 border border-yellow-500/30 rounded-lg text-sm text-yellow-200">
            ⚠️ Connecting to backend... Make sure the Python server is running.
          </div>
        )}
        <div className="flex gap-3">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSend()}
            disabled={thinking || connectionStatus !== 'connected'}
            placeholder="Ask me anything..."
            className="flex-1 bg-gray-800/50 border border-purple-500/30 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:border-purple-500 focus:ring-2 focus:ring-purple-500/20 disabled:opacity-50 disabled:cursor-not-allowed"
          />
          <button
            onClick={handleSend}
            disabled={thinking || !input.trim() || connectionStatus !== 'connected'}
            className="bg-gradient-to-r from-blue-500 to-purple-500 hover:from-blue-600 hover:to-purple-600 disabled:opacity-50 disabled:cursor-not-allowed text-white px-6 py-3 rounded-lg font-semibold flex items-center gap-2 transition-all hover:shadow-lg hover:shadow-purple-500/50"
          >
            {thinking ? (
              <Loader size={20} className="animate-spin" />
            ) : (
              <Send size={20} />
            )}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;
