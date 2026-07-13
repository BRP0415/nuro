const { contextBridge, ipcMain } = require('electron');

contextBridge.exposeInMainWorld('electron', {
  getSystemInfo: () => ipcRenderer.invoke('get-system-info'),
});
