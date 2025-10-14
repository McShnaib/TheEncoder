# Building SPSS Prep Tool as Standalone Executable

This guide explains how to create a standalone `.exe` file for the SPSS Prep Tool.

---

## 📋 Two Options Available

### Option 1: Simple Launcher (Recommended for most users)
- Uses `run_app.bat` batch file
- Requires Python installed on user's computer
- Auto-installs dependencies on first run
- Faster to set up
- Smaller file size

### Option 2: Standalone .exe (Best for distribution)
- Creates single `.exe` file
- No Python installation needed on user's computer
- Includes all dependencies
- Larger file size (~150-200 MB)
- Takes longer to build

---

## Option 1: Simple Launcher (.bat file)

### Steps:

1. **Make sure all files are in the project folder:**
   - `app.py`, `encoder.py`, `sps_generator.py`, `utils.py`
   - `requirements.txt`
   - `launcher.py`
   - `run_app.bat`

2. **Share the entire folder** with users

3. **Users double-click `run_app.bat`:**
   - First run: Automatically installs dependencies
   - Subsequent runs: Launches immediately
   - Opens app in web browser

### Pros:
- ✅ Easy to set up
- ✅ Easy to update (just replace Python files)
- ✅ Small file size
- ✅ Users can see and modify code if needed

### Cons:
- ❌ Requires Python 3.10+ installed
- ❌ Requires internet for dependency installation
- ❌ Multiple files to distribute

---

## Option 2: Standalone Executable (.exe)

### Prerequisites:

- Python 3.10 or higher installed
- All project files
- Internet connection

### Steps:

#### 1. Install PyInstaller (if not already installed)

```bash
pip install pyinstaller
```

#### 2. Run the Build Script

```bash
python build_exe.py
```

This will:
- Check if PyInstaller is installed
- Create a spec file
- Build the executable
- Output to `dist/SPSS_Prep_Tool.exe`

#### 3. Find Your Executable

The `.exe` file will be in: `dist/SPSS_Prep_Tool.exe`

#### 4. Test It

```bash
cd dist
SPSS_Prep_Tool.exe
```

#### 5. Distribute

- Copy `dist/SPSS_Prep_Tool.exe` to wherever you want
- Share the single `.exe` file with users
- Users double-click to run (no installation needed!)

### Pros:
- ✅ Single file distribution
- ✅ No Python installation required on user's computer
- ✅ Includes all dependencies
- ✅ Professional appearance

### Cons:
- ❌ Large file size (~150-200 MB)
- ❌ Slower first-time startup
- ❌ Harder to update (need to rebuild entire .exe)
- ❌ May trigger antivirus warnings (false positives)

---

## 🛠️ Advanced: Manual PyInstaller Build

If the build script doesn't work, you can build manually:

### Basic Build:

```bash
pyinstaller --onefile --name="SPSS_Prep_Tool" launcher.py
```

### Advanced Build with Options:

```bash
pyinstaller ^
    --onefile ^
    --name="SPSS_Prep_Tool" ^
    --add-data "requirements.txt;." ^
    --add-data "app.py;." ^
    --add-data "encoder.py;." ^
    --add-data "sps_generator.py;." ^
    --add-data "utils.py;." ^
    --hidden-import pandas ^
    --hidden-import streamlit ^
    --hidden-import openpyxl ^
    --hidden-import xlsxwriter ^
    --console ^
    launcher.py
```

Note: On Windows, use semicolon `;` in `--add-data`. On Linux/Mac, use colon `:`.

---

## 🎯 Recommended Approach

**For personal use or small team:**
→ Use **Option 1** (Simple Launcher)

**For distribution to non-technical users:**
→ Use **Option 2** (Standalone .exe)

**For open-source / GitHub releases:**
→ Provide both options:
- Source code + `run_app.bat` for developers
- `.exe` file for end users

---

## 📝 What Gets Included

### In the .exe:
- Python interpreter
- All Python packages (pandas, streamlit, etc.)
- Your application code (app.py, encoder.py, etc.)
- Configuration files

### Not included:
- User data
- Generated files (encoded_data.xlsx, .sps files)
- Sample files

---

## 🐛 Troubleshooting

### PyInstaller: ModuleNotFoundError

**Solution:** Add missing module to hidden imports:

```bash
pyinstaller --hidden-import missing_module_name launcher.py
```

### Antivirus Blocks .exe

**Cause:** PyInstaller executables may be flagged as false positives

**Solutions:**
1. Add exception in antivirus
2. Submit to antivirus vendor for whitelisting
3. Code-sign the executable (requires certificate)

### .exe is Too Large

**Solutions:**
1. Use `--onefile` instead of `--onedir`
2. Exclude unnecessary packages with `--exclude-module`
3. Use UPX compression: `--upx-dir=path/to/upx`

### Streamlit Doesn't Launch

**Check:**
1. Make sure all data files are included (`--add-data`)
2. Check hidden imports include all Streamlit dependencies
3. Run with `--console` to see error messages

---

## 📦 Alternative: Create Installer

For even more professional distribution:

### Using NSIS (Nullsoft Scriptable Install System):

1. Install NSIS: https://nsis.sourceforge.io/
2. Create installer script
3. Bundle .exe + shortcuts + uninstaller

### Using Inno Setup:

1. Install Inno Setup: https://jrsoftware.org/isinfo.php
2. Create .iss script
3. Compile to installer.exe

---

## 🔄 Updating the Application

### With .bat launcher:
- Replace Python files
- Users get updates on next run

### With .exe:
- Rebuild entire executable
- Redistribute new .exe
- Consider implementing auto-update mechanism

---

## 📊 File Size Comparison

| Method | Size | Startup Time |
|--------|------|--------------|
| Python scripts only | < 1 MB | Fast |
| .bat launcher | < 1 MB | Fast |
| PyInstaller .exe | 150-200 MB | Slower first run |
| PyInstaller .exe (UPX) | 80-120 MB | Slower first run |

---

## 🎉 Success Checklist

- [ ] Build completes without errors
- [ ] .exe file exists in `dist` folder
- [ ] Double-clicking .exe opens command window
- [ ] Web browser opens with Streamlit app
- [ ] Can upload Excel files
- [ ] Can download encoded files
- [ ] .sps files work in SPSS

---

## 💡 Tips

1. **Test on clean system:** Test the .exe on a computer without Python installed
2. **Include README:** Add usage instructions with the .exe
3. **Version numbering:** Name files like `SPSS_Prep_Tool_v1.1.2.exe`
4. **Keep source:** Always keep the source code for updates
5. **Backup builds:** Save working .exe versions

---

## 📧 Support

If you encounter issues building:

1. Check Python version: `python --version` (need 3.10+)
2. Check PyInstaller version: `pyinstaller --version`
3. Try rebuilding with `--clean` flag
4. Check the `build` folder for error logs
5. Search PyInstaller documentation: https://pyinstaller.org/

---

**Happy building!** 🎊

