# 🚀 How to Build Nuro .EXE (Step-by-Step)

## Prerequisites (One-Time Setup)

You need to install these ONCE:

### 1. Install Node.js

**Windows:**
1. Go to https://nodejs.org/
2. Click "LTS" (Long Term Support)
3. Download the `.msi` file
4. Run the installer, click "Next" through everything
5. Restart your computer

**Verify it worked:**
```
node --version
npm --version
```

You should see version numbers like `v18.17.0`

---

### 2. Install Python

**Windows:**
1. Go to https://python.org/
2. Click "Downloads"
3. Download "Python 3.11" (or latest 3.x)
4. Run the installer
5. **IMPORTANT:** Check the box that says "Add Python to PATH"
6. Click "Install Now"
7. Wait for completion

**Verify it worked:**
```
python --version
```

You should see something like `Python 3.11.5`

---

### 3. Install Git (Optional but Recommended)

**Windows:**
1. Go to https://git-scm.com/
2. Download the Windows installer
3. Run it, click "Next" through everything

---

## Getting Nuro Code

### Option A: Clone with Git (Recommended)

1. Open Command Prompt (`Win + R`, type `cmd`, press Enter)
2. Go to where you want Nuro:
   ```
   cd Desktop
   ```
3. Clone the repository:
   ```
   git clone https://github.com/BRP0415/nuro.git
   cd nuro
   ```

### Option B: Download ZIP

1. Go to https://github.com/BRP0415/nuro
2. Click green "Code" button
3. Click "Download ZIP"
4. Extract the ZIP file
5. Open Command Prompt in that folder

---

## Building the .EXE

### Step 1: Open Command Prompt in the Nuro Folder

```
Win + R
type: cmd
press Enter

type: cd path\to\nuro
(Example: cd C:\Users\YourName\Desktop\nuro)
```

### Step 2: Install Dependencies

```
npm install
```

**What this does:**
- Downloads all JavaScript libraries (~500MB)
- Takes 2-5 minutes
- Creates a `node_modules` folder

### Step 3: Install Python Dependencies

```
cd backend
pip install -r requirements.txt
cd ..
```

**What this does:**
- Downloads Python libraries
- Takes 1-2 minutes

### Step 4: Build the Executable

```
npm run build:exe
```

**What this does:**
1. Builds React frontend (2-3 minutes)
2. Bundles everything together (5-10 minutes)
3. Creates `Nuro.exe` in `dist/` folder

**Total time:** ~15-20 minutes on first build

---

## Your .EXE is Ready!

After the build completes, you'll find:

```
C:\Users\YourName\Desktop\nuro\dist\Nuro.exe
```

That's your standalone executable! 

### **You can now:**

✅ **Share it with anyone** - Just email the `.exe` file  
✅ **Run it on any Windows PC** - No installation needed  
✅ **Double-click to use** - Automatically starts everything  

---

## Troubleshooting

### "npm is not recognized"

**Solution:** Node.js didn't install correctly
1. Uninstall Node.js from Control Panel
2. Restart your computer
3. Reinstall Node.js from https://nodejs.org/
4. **Make sure you restart after installing**

### "python is not recognized"

**Solution:** Python didn't add to PATH
1. Uninstall Python from Control Panel
2. Reinstall Python from https://python.org/
3. **CHECK the box "Add Python to PATH"** during install
4. Restart your computer

### "npm install hangs/fails"

**Solution:** Network or disk space issue
```
npm cache clean --force
rm -r node_modules package-lock.json
npm install
```

### "build:exe fails"

**Check error message and try:**
```
del /s dist build
npm run build:exe
```

If that doesn't work, open a GitHub issue with the error message.

---

## Complete Command Reference

### Just Copy & Paste These

**First Time Setup:**
```batch
REM Clone the code
git clone https://github.com/BRP0415/nuro.git
cd nuro

REM Install dependencies
npm install
cd backend
pip install -r requirements.txt
cd ..

REM Build the exe
npm run build:exe
```

**After Build:**
```
Your .exe is at: dist\Nuro.exe
```

**To rebuild later (changes made):**
```batch
cd C:\path\to\nuro
npm run build:exe
```

---

## What's Happening Behind the Scenes

When you run `npm run build:exe`:

1. **React Build**
   - Compiles your React components
   - Optimizes for production
   - Creates `build/` folder with HTML/CSS/JS

2. **Python Packaging**
   - Uses PyInstaller to bundle Python runtime
   - Bundles all backend code
   - Creates a standalone Python `.exe`

3. **Electron Packaging**
   - Combines frontend + bundled backend
   - Uses Electron to create native Windows app
   - Creates final `Nuro.exe` (~500MB)

4. **Output**
   - `dist/Nuro.exe` - Ready to distribute!

---

## What the User Gets

When someone runs your `Nuro.exe`:

✅ No downloads needed  
✅ No installation  
✅ No prerequisites  
✅ Auto-handles Ollama  
✅ Auto-downloads AI model  
✅ Opens browser with Nuro  
✅ Works completely offline after first run  

---

## Next Steps After Building

### 1. **Test It**
```
C:\Users\YourName\Desktop\nuro\dist\Nuro.exe
```
Double-click and make sure it works!

### 2. **Share It**
- Email to friends
- Upload to GitHub Releases
- Host on your website
- Share on Discord

### 3. **Iterate**
- Make changes to code
- Run `npm run build:exe` again
- Test the new version
- Distribute updated `.exe`

---

## Tips

💡 **First build is slow** (15-20 mins) because it downloads everything  
💡 **Rebuilds are faster** (5-10 mins) because dependencies are cached  
💡 **The .exe is large** (~500MB) because it bundles Python + React  
💡 **Keep the `.exe` alone** - It's completely standalone  

---

## Still Having Issues?

1. Post on GitHub Issues: https://github.com/BRP0415/nuro/issues
2. Include the error message you see
3. Include your OS version (`Win + R` → `winver`)
4. Include Node version (`node --version`)
5. Include Python version (`python --version`)

---

**Good luck! Your .exe will be amazing!** 🚀✨
