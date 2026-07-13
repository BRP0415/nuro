import React, { useState, useEffect } from 'react';
import { MessageCircle, Brain, Settings, Send, Loader } from 'lucide-react';
import ChatInterface from './components/ChatInterface';
import BrainVisualization from './components/BrainVisualization';
import ControlPanel from './components/ControlPanel';
import { useNuroStore } from './store/nuroStore';

function App() {
  const [activeTab, setActiveTab] = useState('chat');
  const { initializeConnection } = useNuroStore();

  useEffect(() => {
    initializeConnection();
  }, []);

  return (
    <div className="h-screen bg-gradient-to-br from-gray-900 via-purple-900 to-black text-white overflow-hidden flex flex-col">
      {/* Header */}
      <div className="border-b border-purple-500/30 px-6 py-4 bg-black/50 backdrop-blur-md">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="text-4xl">✨</div>
            <div>
              <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
                Nuro
              </h1>
              <p className="text-xs text-gray-400 mt-1">Local AI Assistant</p>
            </div>
          </div>
          <div className="flex items-center gap-2 text-sm text-gray-400">
            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
            Connected
          </div>
        </div>
      </div>

      {/* Tab Navigation */}
      <div className="flex gap-2 px-6 py-4 bg-black/30 border-b border-purple-500/20">
        {[
          { id: 'chat', label: 'Chat', icon: MessageCircle },
          { id: 'brain', label: 'Brain', icon: Brain },
          { id: 'control', label: 'Control', icon: Settings },
        ].map(({ id, label, icon: Icon }) => (
          <button
            key={id}
            onClick={() => setActiveTab(id)}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg font-semibold transition-all ${
              activeTab === id
                ? 'bg-gradient-to-r from-blue-500 to-purple-500 text-white shadow-lg shadow-purple-500/50'
                : 'bg-gray-800 text-gray-300 hover:bg-gray-700'
            }`}
          >
            <Icon size={18} />
            {label}
          </button>
        ))}
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-hidden">
        {activeTab === 'chat' && <ChatInterface />}
        {activeTab === 'brain' && <BrainVisualization />}
        {activeTab === 'control' && <ControlPanel />}
      </div>
    </div>
  );
}

export default App;
