import React, { useEffect, useState } from 'react';
import { useNuroStore } from '../store/nuroStore';
import { Activity, Zap, Network } from 'lucide-react';

const BrainVisualization = () => {
  const { brainActivity, thinking, messages } = useNuroStore();
  const [animatedNeurons, setAnimatedNeurons] = useState([]);

  useEffect(() => {
    // Simulate neural activity
    if (thinking) {
      const interval = setInterval(() => {
        setAnimatedNeurons(
          Array.from({ length: 50 }, () => ({
            x: Math.random() * 100,
            y: Math.random() * 100,
            size: Math.random() * 4 + 1,
            opacity: Math.random() * 0.8 + 0.2,
            delay: Math.random() * 0.5,
          }))
        );
      }, 300);
      return () => clearInterval(interval);
    }
  }, [thinking]);

  return (
    <div className="h-full bg-gradient-to-br from-gray-900 via-purple-900/50 to-black p-8 flex flex-col gap-6 overflow-y-auto">
      {/* Neural Network Visualization */}
      <div className="bg-gray-900/50 border border-purple-500/30 rounded-xl p-6 backdrop-blur-sm h-96">
        <div className="flex items-center gap-3 mb-4">
          <Network size={24} className="text-purple-400" />
          <h3 className="text-xl font-bold">Neural Activity</h3>
          {thinking && (
            <span className="ml-auto text-sm text-purple-300 animate-pulse">Active</span>
          )}
        </div>

        <svg className="w-full h-full" viewBox="0 0 100 100">
          {/* Background nodes */}
          <defs>
            <radialGradient id="neuronGradient">
              <stop offset="0%" stopColor="#a78bfa" stopOpacity="0.8" />
              <stop offset="100%" stopColor="#7c3aed" stopOpacity="0.3" />
            </radialGradient>
          </defs>

          {/* Draw neurons */}
          {animatedNeurons.map((neuron, i) => (
            <g key={i}>
              <circle
                cx={neuron.x}
                cy={neuron.y}
                r={neuron.size}
                fill="url(#neuronGradient)"
                opacity={neuron.opacity}
                style={{
                  animation: `pulse 2s ease-in-out infinite`,
                  animationDelay: `${neuron.delay}s`,
                }}
              />
              {/* Connections */}
              {i % 3 === 0 && i < animatedNeurons.length - 1 && (
                <line
                  x1={neuron.x}
                  y1={neuron.y}
                  x2={animatedNeurons[(i + 1) % animatedNeurons.length].x}
                  y2={animatedNeurons[(i + 1) % animatedNeurons.length].y}
                  stroke="#a78bfa"
                  strokeWidth="0.2"
                  opacity={Math.random() * 0.3 + 0.1}
                />
              )}
            </g>
          ))}
        </svg>
      </div>

      {/* Brain Stats */}
      <div className="grid grid-cols-3 gap-4">
        {[
          {
            icon: Activity,
            label: 'Processing Speed',
            value: thinking ? 'Active' : 'Idle',
            color: 'text-green-400',
          },
          {
            icon: Zap,
            label: 'Token Generation',
            value: `${messages.length * 50}`,
            color: 'text-yellow-400',
          },
          {
            icon: Network,
            label: 'Neurons Active',
            value: animatedNeurons.length,
            color: 'text-purple-400',
          },
        ].map(({ icon: Icon, label, value, color }, i) => (
          <div
            key={i}
            className="bg-gray-900/50 border border-purple-500/30 rounded-lg p-4 backdrop-blur-sm"
          >
            <Icon size={20} className={`${color} mb-2`} />
            <p className="text-sm text-gray-400">{label}</p>
            <p className={`text-2xl font-bold ${color}`}>{value}</p>
          </div>
        ))}
      </div>

      {/* Thought Process */}
      <div className="bg-gray-900/50 border border-purple-500/30 rounded-lg p-6 backdrop-blur-sm">
        <h4 className="font-bold mb-4 flex items-center gap-2">
          <span className="text-purple-400">🧠</span>
          Thinking Process
        </h4>
        <div className="space-y-2 text-sm text-gray-400">
          {thinking ? (
            <>
              <div className="flex items-center gap-2 animate-pulse">
                <span className="inline-block w-2 h-2 bg-purple-400 rounded-full"></span>
                Loading context...
              </div>
              <div className="flex items-center gap-2 animate-pulse" style={{ animationDelay: '0.2s' }}>
                <span className="inline-block w-2 h-2 bg-blue-400 rounded-full"></span>
                Analyzing request...
              </div>
              <div className="flex items-center gap-2 animate-pulse" style={{ animationDelay: '0.4s' }}>
                <span className="inline-block w-2 h-2 bg-pink-400 rounded-full"></span>
                Generating response...
              </div>
            </>
          ) : (
            <p className="text-gray-500">Send a message to see thinking process</p>
          )}
        </div>
      </div>

      <style>{`
        @keyframes pulse {
          0%, 100% { opacity: 0.3; }
          50% { opacity: 0.8; }
        }
      `}</style>
    </div>
  );
};

export default BrainVisualization;
