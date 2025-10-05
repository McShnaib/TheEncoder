"""
SPSS Prep Tool - Standalone Launcher
This script checks dependencies and launches the Streamlit app.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is adequate."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print("❌ Python 3.10 or higher is required!")
        print(f"   Current version: {version.major}.{version.minor}.{version.micro}")
        print("\n📥 Download Python from: https://www.python.org/downloads/")
        input("\nPress Enter to exit...")
        sys.exit(1)
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")


def check_and_install_requirements():
    """Check if all required packages are installed, install if missing."""
    print("\n📦 Checking dependencies...")
    
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if not requirements_file.exists():
        print("❌ requirements.txt not found!")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Read requirements
    with open(requirements_file, 'r') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    # Check if pip is available
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', '--version'], 
                            stdout=subprocess.DEVNULL, 
                            stderr=subprocess.DEVNULL)
    except:
        print("❌ pip is not available!")
        input("Press Enter to exit...")
        sys.exit(1)
    
    # Try importing packages
    missing_packages = []
    installed_packages = []
    
    for req in requirements:
        # Extract package name (before ==, >=, etc.)
        package_name = req.split('==')[0].split('>=')[0].split('<')[0].strip()
        
        try:
            __import__(package_name.replace('-', '_'))
            installed_packages.append(package_name)
            print(f"  ✅ {package_name}")
        except ImportError:
            missing_packages.append(req)
            print(f"  ❌ {package_name} - not installed")
    
    # Install missing packages
    if missing_packages:
        print(f"\n📥 Installing {len(missing_packages)} missing package(s)...")
        print("   This may take a few minutes...")
        
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install'] + missing_packages,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )
            print("✅ All dependencies installed successfully!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install dependencies!")
            print(f"   Error: {e.stderr.decode() if e.stderr else 'Unknown error'}")
            print("\n💡 Try running manually:")
            print(f"   pip install -r requirements.txt")
            input("\nPress Enter to exit...")
            sys.exit(1)
    else:
        print("\n✅ All dependencies are already installed!")


def launch_streamlit():
    """Launch the Streamlit app."""
    print("\n🚀 Launching SPSS Prep Tool...")
    print("   The app will open in your default web browser.")
    print("   Press Ctrl+C in this window to stop the app.\n")
    print("=" * 60)
    
    app_file = Path(__file__).parent / "app.py"
    
    if not app_file.exists():
        print("❌ app.py not found!")
        input("Press Enter to exit...")
        sys.exit(1)
    
    try:
        # Launch Streamlit
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', str(app_file),
            '--server.headless', 'true',
            '--browser.gatherUsageStats', 'false'
        ])
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down SPSS Prep Tool...")
        print("   Thank you for using the app!")
    except Exception as e:
        print(f"\n❌ Error launching app: {e}")
        input("\nPress Enter to exit...")
        sys.exit(1)


def main():
    """Main launcher function."""
    print("=" * 60)
    print("  📊 SPSS Prep Tool - Standalone Launcher")
    print("=" * 60)
    
    # Check Python version
    check_python_version()
    
    # Check and install dependencies
    check_and_install_requirements()
    
    # Launch the app
    launch_streamlit()


if __name__ == "__main__":
    main()

