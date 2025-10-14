# Installation Guide

This guide provides detailed installation instructions for SPSS Prep Tool across different platforms and use cases.

## 📋 Requirements

### System Requirements
- **Python**: 3.10 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: At least 512MB RAM (2GB+ recommended for large datasets)
- **Storage**: 100MB free space

### Software Dependencies
- **For Users**: Only Python is required
- **For Contributors**: Git, Python, and development tools

## 🚀 Installation Methods

### Method 1: PyPI Installation (Recommended for Users)

This is the easiest way for end users who just want to use the tool:

```bash
# Install from PyPI
pip install spss-prep-tool

# Run the application
spss-prep-tool
```

### Method 2: Source Installation (For Contributors)

This method is recommended for developers who want to contribute or modify the code:

#### Step 1: Clone Repository
```bash
git clone https://github.com/your-org/spss-prep-tool.git
cd spss-prep-tool
```

#### Step 2: Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)  
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
# For regular usage
pip install -e .

# For development (includes testing, linting, etc.)
pip install -e ".[dev]"

# For testing only
pip install -e ".[test]"
```

#### Step 4: Set Up Pre-commit Hooks (Optional)
```bash
pre-commit install
```

#### Step 5: Run the Application
```bash
# Method 1: Direct execution
streamlit run src/spss_prep/app.py

# Method 2: Using entry point
spss-prep-tool
```

## 🐳 Docker Installation (Alternative)

For containerized deployment:

```bash
# Build the image
docker build -t spss-prep-tool .

# Run the container
docker run -p 8501:8501 spss-prep-tool
```

## 🖥️ Platform-Specific Instructions

### Windows

1. **Install Python** from [python.org](https://python.org) (check "Add to PATH")
2. **Open Command Prompt** or PowerShell
3. **Follow installation steps** above

Common Windows issues:
- If `pip` isn't recognized, try `python -m pip` instead
- Use `python` instead of `python3`
- Antivirus might block installation - add Python to exceptions

### macOS

1. **Install Python** using homebrew or from python.org:
   ```bash
   brew install python3
   ```
2. **Open Terminal**
3. **Follow installation steps** above

### Linux (Ubuntu/Debian)

1. **Install Python and pip**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```
2. **Follow installation steps** above

### Linux (CentOS/RHEL/Fedora)

1. **Install Python and pip**:
   ```bash
   # CentOS/RHEL
   sudo yum install python3 python3-pip
   
   # Fedora
   sudo dnf install python3 python3-pip
   ```
2. **Follow installation steps** above

## 🔧 Development Setup

For contributors who want the full development environment:

### 1. Fork and Clone
```bash
# Fork the repo on GitHub first, then:
git clone https://github.com/YOUR-USERNAME/spss-prep-tool.git
cd spss-prep-tool
```

### 2. Install Development Tools
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install all development dependencies
pip install -e ".[dev]"

# Set up pre-commit hooks
pre-commit install
```

### 3. Verify Installation
```bash
# Run tests
pytest tests/ -v

# Check code formatting
black --check src/ tests/
flake8 src/ tests/
isort --check-only src/ tests/

# Run the application
streamlit run src/spss_prep/app.py
```

## ✅ Verification

After installation, verify everything works:

### 1. Check Version
```bash
python -c "import spss_prep; print(spss_prep.__version__)"
```

### 2. Run Tests (Development Installation)
```bash
pytest tests/ -v
```

### 3. Start Application
```bash
spss-prep-tool
```
- Should open browser to `http://localhost:8501`
- Try uploading `sample_input.xlsx`

## 🐛 Troubleshooting

### Common Issues

#### "Module not found" errors
```bash
# Make sure you're in the right directory
cd spss-prep-tool

# Reinstall in development mode
pip install -e .
```

#### Streamlit won't start
```bash
# Check if streamlit is installed
pip list | grep streamlit

# Reinstall streamlit
pip install --upgrade streamlit
```

#### Permission errors on Windows
- Run Command Prompt as Administrator
- Or install for user only: `pip install --user spss-prep-tool`

#### Python version conflicts
```bash
# Check Python version
python --version

# Use specific Python version
python3.11 -m pip install spss-prep-tool
```

### Getting Help

If you encounter issues:

1. **Check existing issues**: [GitHub Issues](https://github.com/your-org/spss-prep-tool/issues)
2. **Search documentation**: This file and [README.md](README.md)
3. **Create new issue**: Include your OS, Python version, and error messages
4. **Ask the community**: [GitHub Discussions](https://github.com/your-org/spss-prep-tool/discussions)

## 🔄 Updating

### Update from PyPI
```bash
pip install --upgrade spss-prep-tool
```

### Update from Source
```bash
cd spss-prep-tool
git pull origin main
pip install -e ".[dev]"
```

## 🗑️ Uninstalling

### Remove PyPI Installation
```bash
pip uninstall spss-prep-tool
```

### Remove Source Installation
```bash
# Deactivate virtual environment
deactivate

# Remove directory
cd ..
rm -rf spss-prep-tool  # Linux/macOS
rmdir /s spss-prep-tool  # Windows
```

---

## 💡 Tips

- **Use virtual environments** to avoid conflicts
- **Pin versions** for reproducible environments
- **Keep dependencies updated** for security
- **Read the logs** when things go wrong
- **Test after installation** to catch issues early

---

*For more help, see [README.md](README.md) or [CONTRIBUTING.md](CONTRIBUTING.md)*
