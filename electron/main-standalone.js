const { app, BrowserWindow, Menu } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const http = require('http');

let mainWindow;
let pythonProcess;
let serverReady = false;

function waitForServer(maxAttempts = 30) {
  return new Promise((resolve) => {
    let attempts = 0;
    const checkServer = () => {
      const req = http.get('http://localhost:8000/api/health', (res) => {
        if (res.statusCode === 200) {
          serverReady = true;
          resolve(true);
        } else {
          attemptConnection();
        }
      });
      req.on('error', attemptConnection);
      req.setTimeout(1000);
    };

    const attemptConnection = () => {
      attempts++;
      if (attempts < maxAttempts) {
        setTimeout(checkServer, 500);
      } else {
        resolve(false);
      }
    };

    checkServer();
  });
}

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    minWidth: 1000,
    minHeight: 700,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      enableRemoteModule: false,
    },
    icon: path.join(__dirname, '../public/nuro.png'),
  });

  // Load from build folder (production) or localhost (dev)
  const startUrl = process.env.NODE_ENV === 'development'
    ? 'http://localhost:3000'
    : `file://${path.join(__dirname, '../build/index.html')}`;

  mainWindow.loadURL(startUrl);

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

function startPythonBackend() {
  const isDev = process.env.NODE_ENV === 'development';
  let pythonPath;

  if (isDev) {
    // Development: assume python is in PATH
    pythonPath = 'python';
  } else {
    // Production: bundled executable
    pythonPath = path.join(path.dirname(app.getAppPath()), 'backend', 'nuro_backend.exe');
    if (!require('fs').existsSync(pythonPath)) {
      pythonPath = 'python'; // Fallback
    }
  }

  pythonProcess = spawn(pythonPath);

  pythonProcess.stdout.on('data', (data) => {
    console.log(`[Backend] ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`[Backend Error] ${data}`);
  });

  pythonProcess.on('error', (err) => {
    console.error('Failed to start backend:', err);
  });
}

app.on('ready', async () => {
  console.log('🚀 Nuro Starting...');
  startPythonBackend();
  
  console.log('⏳ Waiting for backend...');
  const ready = await waitForServer();
  
  if (ready) {
    console.log('✅ Backend ready, creating window...');
    createWindow();
  } else {
    console.error('❌ Backend failed to start');
    process.exit(1);
  }
});

app.on('window-all-closed', () => {
  if (pythonProcess) {
    pythonProcess.kill();
  }
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});
