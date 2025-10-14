# SPSS Prep Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io/)

A **Streamlit web application** for automating the preparation of Google Forms Excel exports for analysis in **IBM SPSS**. This tool detects categorical options, allows users to configure and reorder them, encodes them into numeric codes, and generates both an encoded Excel file and an SPSS syntax file (`.sps`) for seamless import.

🎯 **Perfect for researchers, data analysts, and students working with survey data!**

---

## 🚀 Quickstart

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-org/spss-prep-tool.git
   cd spss-prep-tool
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run src/spss_prep/app.py
   ```

5. **Open your browser** to the URL shown (typically `http://localhost:8501`)

#### Quick Demo

Try it with the included sample data:
```bash
# After installation, upload examples/sample_input.xlsx in the web interface
```

---

## 📋 Features

- **📤 Upload Excel files** - Import Google Forms exports (`.xlsx`)
- **🔍 Automatic detection** - Identifies unique values per column
- **🎯 Smart heuristics** - Detects likely Likert scales automatically
- **↕️ Reorder options** - Use Up/Down buttons to arrange response order
- **🔢 Flexible encoding** - Configure start values and direction (ascending/descending)
- **✅ Interactive TODO** - Visual progress checklist in sidebar
- **📊 Encoding types** - Support for Likert (ordinal), Nominal, and Ignore
- **🏷️ Variable sanitization** - Auto-converts column names to SPSS-compatible format
- **⚠️ Multi-response detection** - Warns about checkbox-style questions
- **📜 SPSS syntax generation** - Creates complete `.sps` import script with VALUE LABELS
- **💾 Download files** - Get both encoded Excel and SPSS syntax files

---

## 🎯 How to Use

### Step 1: Upload Your Data

- Click "Upload your Google Forms export (.xlsx)"
- Select an Excel file exported from Google Forms (or any similar survey data)
- The app will show a preview of the first 5 rows

### Step 2: Configure Column Encodings

For each detected column, the app shows an expandable configuration card where you can:

1. **View column metadata:**
   - Number of unique values
   - Missing value count
   - Detected type (numeric, Likert-scale, multi-response, etc.)

2. **Configure SPSS variable name:**
   - The sanitized name is shown and editable
   - Names are automatically made SPSS-compatible (letters, digits, underscore only)
   - Maximum 64 characters

3. **Select encoding type:**
   - **Likert**: Ordinal scale (responses have meaningful order)
   - **Nominal**: Categorical (no inherent order)
   - **Ignore**: Skip this column (won't be encoded)

4. **Set encoding parameters:**
   - **Start Value**: The first numeric code (default: 1)
   - **Direction**: 
     - *Ascending*: First option → smallest number
     - *Descending*: First option → largest number

5. **Reorder response options:**
   - Use **↑** and **↓** buttons to rearrange options
   - The order determines which response gets which numeric code
   - See a live preview of the mapping below

6. **Configure missing values:**
   - Toggle "Treat missing/blank as system-missing" (recommended: checked)

### Step 3: Apply Encoding

- Click **"🚀 Apply Encoding & Generate Files"**
- The app will:
  1. Encode all configured columns to numeric values
  2. Generate `encoded_data.xlsx`
  3. Generate `auto_import.sps` (SPSS syntax file)

### Step 4: Preview & Download

- **Preview the encoded data** - See the first few rows with numeric codes
- **Preview the SPSS syntax** - Review the generated `.sps` script
- **Download both files** using the download buttons

### Step 5: Use in SPSS

1. Open **IBM SPSS Statistics**
2. Go to **File → Open → Syntax**
3. Open the downloaded `auto_import.sps` file
4. Click **Run → All** (or press Ctrl+A, then Ctrl+R)
5. SPSS will:
   - Import the encoded Excel file
   - Apply value labels (numeric codes → original text)
   - Optionally save a `.sav` file (if enabled in settings)

---

## ⚙️ Settings (Sidebar)

### Include SAVE OUTFILE
- **Default:** Off
- **Purpose:** Adds a `SAVE OUTFILE` command to the `.sps` to create a `.sav` file
- **Note:** The `.sav` path will be next to the encoded Excel file

### Write .sps to same folder as encoded file
- **Default:** On
- **Purpose:** Places the `.sps` file in the same directory as `encoded_data.xlsx`

### Sanitize variable names for SPSS
- **Default:** On
- **Purpose:** Converts column names to SPSS-compatible format
- **Rules applied:**
  - Starts with a letter
  - Contains only letters, digits, and underscores
  - Maximum 64 characters
  - Replaces spaces and special characters with underscore
  - Removes consecutive underscores

---

## 📁 Project Structure

```
spss-prep-tool/
├── src/
│   └── spss_prep/            # Main package
│       ├── __init__.py
│       ├── app.py            # Streamlit application
│       ├── encoder.py        # Data encoding logic
│       ├── sps_generator.py  # SPSS syntax generation
│       └── utils.py          # Helper utilities
├── tests/                    # Test suite
│   └── test_encoding.py      # Unit tests
├── .github/workflows/        # CI/CD automation
├── docs/                     # Documentation
├── examples/                 # Example files
├── sample_input.xlsx         # Sample survey data
├── requirements.txt          # Runtime dependencies
├── requirements-dev.txt      # Development dependencies
├── pyproject.toml           # Package configuration
├── LICENSE                  # MIT License
├── README.md               # This documentation
├── CONTRIBUTING.md         # Contribution guidelines
├── CODE_OF_CONDUCT.md      # Community standards
├── CHANGELOG              # Version history
└── TODO.md                # Development roadmap
```

---

## 🧪 Testing

Run the test suite with pytest:

```bash
pytest tests/ -v
```

Tests cover:
- Variable name sanitization
- SPSS string escaping
- Likert scale detection
- Encoding mapping generation
- VALUE LABELS block generation
- Missing value handling

---

## 📊 Example SPSS Syntax Output

```spss
* Auto-generated by SPSS Prep Tool
* This script imports encoded data and applies value labels
* Original column names are preserved as variable labels

GET DATA
  /TYPE=XLSX
  /FILE="C:\\Users\\YourName\\Documents\\encoded_data.xlsx"
  /SHEET=name "Sheet1"
  /READNAMES=ON.

VALUE LABELS
  q1 1 'Strongly Disagree' 2 'Disagree' 3 'Neutral' 4 'Agree' 5 'Strongly Agree' /
  q2 1 'Never' 2 'Rarely' 3 'Sometimes' 4 'Often' 5 'Always'.

VARIABLE LABELS
  q1 'How satisfied are you with our service?' /
  q2 'How often do you use our product?'.

EXECUTE.
```

---

## 🔧 Design Decisions & Assumptions

### Variable Name Sanitization
- Maximum length: **64 characters** (SPSS limit)
- Invalid characters replaced with underscore
- If name doesn't start with letter, prefix with `v_`

### Encoding Defaults
- Default start value: **1** (most common in SPSS)
- Default direction: **Ascending**
- Missing/blank cells: Left as empty (system-missing) by default

### Multi-Response Columns
- **Phase 1 limitation:** Multi-response columns (containing commas/semicolons) are detected but treated as atomic strings
- Future versions will support automatic dummy variable creation

### Path Handling
- All paths in `.sps` files are **absolute paths**
- Backslashes are doubled for Windows compatibility (`C:\\path\\to\\file.xlsx`)
- Forward slashes work on both Windows and Unix

### Likert Detection Heuristic
- Columns with 3-7 unique values are checked
- Keywords matched: "agree", "disagree", "never", "always", "satisfied", etc.
- Detection is case-insensitive

---

## ⚠️ Limitations & Known Issues

1. **Multi-response splitting not implemented** - Checkbox-style questions with multiple selections are treated as single strings
2. **No Google Forms API integration** - Must manually export and upload Excel files
3. **Local operation only** - Does not execute SPSS commands (generates syntax only)
4. **Excel format only** - Currently supports `.xlsx` only (not `.xls` or `.csv`)

See `TODO.md` for planned improvements.

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### What this means:
- ✅ **Free to use** for personal and commercial projects
- ✅ **Free to modify** and distribute
- ✅ **No warranty** - use at your own risk
- ✅ **Attribution required** - please keep the license notice

### Citation

If you use this tool in academic research, please cite:

```bibtex
@software{spss_prep_tool,
  title = {SPSS Prep Tool: Automated Survey Data Preparation},
  author = {SPSS Prep Tool Contributors},
  year = {2025},
  url = {https://github.com/your-org/spss-prep-tool},
  version = {1.2.0}
}
```

---

## 🤝 Contributing

We welcome contributions from the community! Whether you're fixing bugs, adding features, improving documentation, or reporting issues, your help is appreciated.

### Quick Start for Contributors

1. 🍴 **Fork the repository** on GitHub
2. 🔧 **Set up your development environment:**
   ```bash
   git clone https://github.com/your-username/spss-prep-tool.git
   cd spss-prep-tool
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   pre-commit install
   ```
3. 🌟 **Create a feature branch:** `git checkout -b feature/amazing-feature`
4. ✅ **Make your changes and add tests**
5. 🧪 **Run tests:** `pytest tests/ -v`
6. 📝 **Update documentation** if needed
7. 🚀 **Submit a pull request**

### What We Need Help With

- 🐛 **Bug reports** and fixes
- ✨ **New features** (see our [TODO.md](TODO.md))
- 🌐 **Internationalization** (especially for non-English surveys)
- 📚 **Documentation** improvements
- 🧪 **More test coverage**
- 🎨 **UI/UX improvements**

For detailed guidelines, see [CONTRIBUTING.md](docs/CONTRIBUTING.md).

### Code of Conduct

Please note that this project is governed by our [Code of Conduct](docs/CODE_OF_CONDUCT.md). By participating, you agree to abide by its terms.

---

## 📧 Support & Community

### Getting Help

- 📖 **Documentation**: Start with this README and [QUICKSTART.md](docs/QUICKSTART.md)
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/your-org/spss-prep-tool/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/your-org/spss-prep-tool/discussions)
- 🏗️ **Development**: See [TODO.md](docs/TODO.md) for roadmap and [CHANGELOG](docs/CHANGELOG.md) for recent changes

### Community

- 🌟 **Star the project** if you find it useful!
- 🐦 **Share** with your research community
- 📢 **Spread the word** about SPSS Prep Tool

### Commercial Support

For organizations needing custom features, training, or consulting services, please open an issue with the "commercial-support" label.

---

## 🙏 Acknowledgments

Built with ❤️ and:
- [Streamlit](https://streamlit.io/) - Web application framework
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- [OpenPyXL](https://openpyxl.readthedocs.io/) - Excel file handling
- [Python](https://python.org/) - The programming language that makes it all possible

Special thanks to:
- The research community for feedback and suggestions
- Contributors who made this tool better
- The open-source ecosystem that makes projects like this possible

### Inspiration

This tool was created to bridge the gap between modern survey platforms (like Google Forms) and traditional statistical software (like SPSS), making data analysis more accessible to researchers worldwide.

---

**Happy analyzing! 📊✨**

