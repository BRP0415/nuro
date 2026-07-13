import React, { useState } from 'react';
import { Shield, AlertCircle, CheckCircle, Settings as SettingsIcon } from 'lucide-react';
import { useNuroStore } from '../store/nuroStore';

const ControlPanel = () => {
  const { aiControlEnabled, toggleAIControl, systemStatus } = useNuroStore();
  const [permissions, setPermissions] = useState({
    mouse: true,
    keyboard: true,
    screenshots: true,
    fileSystem: false,
  });

  return (
    <div className="h-full bg-gradient-to-br from-gray-900 via-purple-900/50 to-black p-8 overflow-y-auto space-y-6">
      {/* AI Control Toggle */}
      <div className="bg-gray-900/50 border border-purple-500/30 rounded-lg p-6 backdrop-blur-sm">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-xl font-bold flex items-center gap-2">
            <Shield size={24} className="text-purple-400" />
            AI Control Status
          </h3>
          <button
            onClick={toggleAIControl}
            className={`relative inline-flex h-8 w-14 items-center rounded-full transition-colors ${
              aiControlEnabled
                ? 'bg-green-600 hover:bg-green-700'
                : 'bg-red-600 hover:bg-red-700'
            }`}
          >
            <span
              className={`inline-block h-6 w-6 transform rounded-full bg-white transition-transform ${
                aiControlEnabled ? 'translate-x-7' : 'translate-x-1'
              }`}
            />
          </button>
        </div>
        <p
          className={`text-sm ${
            aiControlEnabled ? 'text-green-300' : 'text-red-300'
          }`}
        >
          {aiControlEnabled
            ? '✓ AI can control your computer when you approve actions'
            : '✗ AI control is disabled'}
        </p>
      </div>

      {/* Permissions */}
      <div className="bg-gray-900/50 border border-purple-500/30 rounded-lg p-6 backdrop-blur-sm">
        <h3 className="text-lg font-bold mb-4 flex items-center gap-2">
          <SettingsIcon size={20} className="text-blue-400" />
          Permissions
        </h3>
        <div className="space-y-3">
          {[
            { key: 'mouse', label: 'Mouse Control', icon: '🖱️' },
            { key: 'keyboard', label: 'Keyboard Control', icon: '⌨️' },
            { key: 'screenshots', label: 'Screenshot Access', icon: '📸' },
            { key: 'fileSystem', label: 'File System Access', icon: '📁' },
          ].map(({ key, label, icon }) => (
            <label key={key} className="flex items-center gap-3 cursor-pointer p-3 rounded-lg hover:bg-gray-800/50 transition-colors">
              <input
                type="checkbox"
                checked={permissions[key]}
                onChange={(e) =>
                  setPermissions({ ...permissions, [key]: e.target.checked })
                }
                className="w-5 h-5 rounded border-purple-500/50 bg-gray-700 cursor-pointer"
              />
              <span className="text-lg">{icon}</span>
              <span className="text-sm font-medium">{label}</span>
            </label>
          ))}
        </div>
      </div>

      {/* System Status */}
      <div className="bg-gray-900/50 border border-purple-500/30 rounded-lg p-6 backdrop-blur-sm">
        <h3 className="text-lg font-bold mb-4">System Status</h3>
        <div className="space-y-3">
          {[
            {
              label: 'Backend Server',
              status: true,
              icon: CheckCircle,
              color: 'text-green-400',
            },
            {
              label: 'AI Model',
              status: systemStatus.modelLoaded,
              icon: systemStatus.modelLoaded ? CheckCircle : AlertCircle,
              color: systemStatus.modelLoaded ? 'text-green-400' : 'text-yellow-400',
            },
            {
              label: 'GPU Support',
              status: true,
              icon: CheckCircle,
              color: 'text-blue-400',
            },
          ].map(({ label, status, icon: Icon, color }, i) => (
            <div key={i} className="flex items-center justify-between p-3 rounded-lg bg-gray-800/30">
              <span className="text-sm text-gray-300">{label}</span>
              <Icon size={20} className={color} />
            </div>
          ))}
        </div>
      </div>

      {/* Information Box */}
      <div className="bg-blue-500/10 border border-blue-500/30 rounded-lg p-4">
        <h4 className="font-semibold mb-2 flex items-center gap-2 text-blue-300">
          <AlertCircle size={18} />
          Privacy & Safety
        </h4>
        <ul className="text-sm text-blue-200/80 space-y-1">
          <li>✓ All processing happens locally on your machine</li>
          <li>✓ No data is sent to external servers</li>
          <li>✓ You can disable AI control at any time</li>
          <li>✓ AI requests confirmation for sensitive actions</li>
        </ul>
      </div>
    </div>
  );
};

export default ControlPanel;
