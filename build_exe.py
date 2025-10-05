"""
Build script to create a standalone .exe using PyInstaller.
This creates a single executable that includes all dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_pyinstaller():
    """Check if PyInstaller is installed."""
    try:
        import PyInstaller
        print("✅ PyInstaller is installed")
        return True
    except ImportError:
        print("❌ PyInstaller is not installed")
        print("\n📥 Installing PyInstaller...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])
            print("✅ PyInstaller installed successfully!")
            return True
        except:
            print("❌ Failed to install PyInstaller")
            print("   Please install manually: pip install pyinstaller")
            return False


def create_spec_file():
    """Create a PyInstaller spec file for the app."""
    spec_content = """# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Collect all necessary data files
datas = [
    ('requirements.txt', '.'),
]

# Hidden imports needed for the app
hiddenimports = [
    'pandas',
    'openpyxl',
    'xlsxwriter',
    'streamlit',
    'altair',
    'pyarrow',
    'pydeck',
    'gitpython',
    'watchdog',
    'tenacity',
    'toml',
]

a = Analysis(
    ['launcher.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Include all Python files
a.datas += Tree('.', prefix='app', excludes=['__pycache__', '*.pyc', '.git', 'dist', 'build', '*.spec'])

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SPSS_Prep_Tool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    coerce_archive_mode=True,
    icon=None,
)
"""
    
    spec_file = Path('SPSS_Prep_Tool.spec')
    with open(spec_file, 'w') as f:
        f.write(spec_content)
    
    print(f"✅ Created spec file: {spec_file}")
    return spec_file


def build_executable():
    """Build the executable using PyInstaller."""
    print("\n🔨 Building executable...")
    print("   This will take several minutes...")
    print("   Output will be in the 'dist' folder\n")
    
    spec_file = create_spec_file()
    
    try:
        # Run PyInstaller
        subprocess.check_call([
            sys.executable, '-m', 'PyInstaller',
            '--clean',
            str(spec_file)
        ])
        
        print("\n✅ Build successful!")
        print("\n📁 Executable location:")
        print(f"   {Path('dist/SPSS_Prep_Tool.exe').absolute()}")
        print("\n📋 Next steps:")
        print("   1. Go to the 'dist' folder")
        print("   2. Copy SPSS_Prep_Tool.exe to wherever you want")
        print("   3. Double-click SPSS_Prep_Tool.exe to run!")
        print("\n💡 Note: First run will install dependencies automatically")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed!")
        print(f"   Error: {e}")
        return False


def main():
    """Main build function."""
    print("=" * 60)
    print("  SPSS Prep Tool - Executable Builder")
    print("=" * 60)
    print()
    
    # Check PyInstaller
    if not check_pyinstaller():
        print("\n❌ Cannot proceed without PyInstaller")
        input("Press Enter to exit...")
        return
    
    print("\n⚙️ This will create a standalone .exe file")
    print("   The .exe will include Python and all dependencies")
    print("   Size: Approximately 150-200 MB")
    print()
    
    response = input("Continue? (y/n): ")
    if response.lower() != 'y':
        print("Build cancelled.")
        return
    
    # Build
    success = build_executable()
    
    if success:
        print("\n🎉 Done!")
    else:
        print("\n❌ Build failed. Check errors above.")
    
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()

