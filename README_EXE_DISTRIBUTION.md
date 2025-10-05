# SPSS Prep Tool - Executable Distribution Guide

## 📦 For End Users

### How to Run SPSS Prep Tool

**Option A: Using the .bat Launcher (Requires Python)**

1. Make sure Python 3.10 or higher is installed
2. Double-click `run_app.bat`
3. First run will install dependencies (takes a few minutes)
4. App opens in your web browser
5. Use the app to encode your survey data!

**Option B: Using the Standalone .exe (No Python Required)**

1. Download `SPSS_Prep_Tool.exe`
2. Double-click to run
3. App opens in your web browser
4. Use the app to encode your survey data!

---

## 🎯 Quick Start

### For Users with Python Installed:

```
1. Unzip the folder
2. Double-click: run_app.bat
3. Wait for dependencies to install (first time only)
4. App opens in browser automatically
```

### For Users without Python:

```
1. Download: SPSS_Prep_Tool.exe
2. Double-click the .exe file
3. App opens in browser automatically
```

---

## ⚠️ Common Issues

### "Python is not recognized..."
**Solution:** Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### "Windows protected your PC"
**Cause:** Windows SmartScreen doesn't recognize the app
**Solution:** 
1. Click "More info"
2. Click "Run anyway"
3. This is safe - it's a false positive

### Antivirus Blocks the .exe
**Cause:** Some antivirus programs flag PyInstaller executables
**Solution:**
1. Add exception in your antivirus
2. Or use the .bat launcher instead (requires Python)

### App Opens then Closes Immediately
**Solution:**
1. Open Command Prompt
2. Navigate to the folder
3. Run: `SPSS_Prep_Tool.exe` to see error messages
4. Make sure no other apps are using port 8501

---

## 📋 System Requirements

### Minimum:
- **OS:** Windows 10 or higher (64-bit)
- **RAM:** 4 GB
- **Disk Space:** 500 MB free
- **Internet:** Required for first-time dependency installation

### Recommended:
- **OS:** Windows 10/11 (64-bit)
- **RAM:** 8 GB
- **Disk Space:** 1 GB free
- **Browser:** Chrome, Edge, or Firefox

---

## 🔒 Security & Privacy

- ✅ All processing is **local** on your computer
- ✅ No data is sent to the internet
- ✅ No tracking or analytics
- ✅ No account required
- ✅ Your data stays private

---

## 📝 What Files Get Created?

When you use the app, it creates:
- `encoded_data.xlsx` - Your encoded survey data
- `auto_import.sps` - SPSS import script

Both files are saved to your Downloads folder (or wherever you save them).

---

## 💡 Updating the App

### If using .bat launcher:
- Download new version
- Replace old files with new ones
- Run `run_app.bat`

### If using .exe:
- Download new .exe file
- Replace old .exe
- Run the new version

---

## 🆘 Getting Help

If you encounter problems:

1. **Check this guide** for common issues above
2. **Try the alternative method** (.bat if .exe doesn't work, or vice versa)
3. **Check the error message** carefully
4. **Make sure you have the latest version**

---

## 🎓 How to Use the App

See the main `README.md` or `QUICKSTART.md` for:
- How to prepare your survey data
- How to configure column encodings
- How to use the generated .sps file in SPSS
- Tips and best practices

---

## 📞 Technical Support

- **Documentation:** See README.md
- **Quick Guide:** See QUICKSTART.md
- **Troubleshooting:** See this file (above)

---

**Enjoy using SPSS Prep Tool!** 📊✨

