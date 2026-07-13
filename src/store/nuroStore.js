import create from 'zustand';

export const useNuroStore = create((set, get) => ({
  messages: [],
  thinking: false,
  connectionStatus: 'connecting',
  brainActivity: [],
  aiControlEnabled: true,
  systemStatus: {
    modelLoaded: false,
    backendRunning: false,
    modelName: 'Loading...',
  },

  // WebSocket connection
  ws: null,
  initializeConnection: () => {
    try {
      const ws = new WebSocket('ws://localhost:8000/ws/chat');

      ws.onopen = () => {
        set({ connectionStatus: 'connected' });
        console.log('Connected to Nuro backend');
      };

      ws.onmessage = (event) => {
        const data = JSON.parse(event.data);

        if (data.type === 'token') {
          set((state) => {
            const messages = [...state.messages];
            if (messages[messages.length - 1]?.role === 'assistant') {
              messages[messages.length - 1].content = data.full;
            }
            return { messages };
          });
        } else if (data.type === 'brain_state') {
          set({ brainActivity: data.activity || [] });
        } else if (data.type === 'done') {
          set({ thinking: false });
        } else if (data.type === 'error') {
          console.error('Backend error:', data.error);
        }
      };

      ws.onerror = (error) => {
        set({ connectionStatus: 'error' });
        console.error('WebSocket error:', error);
      };

      ws.onclose = () => {
        set({ connectionStatus: 'disconnected' });
        console.log('Disconnected from Nuro backend');
      };

      set({ ws });
    } catch (error) {
      console.error('Failed to initialize connection:', error);
      set({ connectionStatus: 'error' });
    }
  },

  sendMessage: (content) => {
    set((state) => ({
      messages: [...state.messages, { role: 'user', content }],
      thinking: true,
    }));
    set((state) => ({
      messages: [
        ...state.messages,
        { role: 'assistant', content: '', thinking: true },
      ],
    }));

    const ws = get().ws;
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({ type: 'message', content }));
    }
  },

  toggleAIControl: () => {
    set((state) => ({ aiControlEnabled: !state.aiControlEnabled }));
  },

  updateSystemStatus: (status) => {
    set((state) => ({
      systemStatus: { ...state.systemStatus, ...status },
    }));
  },
}));
