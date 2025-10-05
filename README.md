# SPSS Prep Tool

A **Streamlit web application** for automating the preparation of Google Forms Excel exports for analysis in **IBM SPSS**. This tool detects categorical options, allows users to configure and reorder them, encodes them into numeric codes, and generates both an encoded Excel file and an SPSS syntax file (`.sps`) for seamless import.

---

## 🚀 Quickstart

### Installation

1. **Clone or download this repository**

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the application:**

```bash
streamlit run app.py
```

4. **Open your browser** to the URL shown (typically `http://localhost:8501`)

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

## 📁 File Structure

```
spss_prep/
├── app.py                    # Main Streamlit application
├── encoder.py                # Encoding logic and detection
├── sps_generator.py          # SPSS syntax generation
├── utils.py                  # Helper utilities
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── TODO.md                   # Project TODO list
├── CHANGELOG                 # Design decisions log
├── sample_input.xlsx         # Sample data file
└── tests/
    └── test_encoding.py      # Unit tests
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

This tool is provided as-is for educational and research purposes.

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

---

## 📧 Support

For issues or questions, please check:
- `TODO.md` for known limitations
- `CHANGELOG` for recent changes
- Test files for usage examples

---

## 🙏 Acknowledgments

Built with:
- [Streamlit](https://streamlit.io/) - Web application framework
- [Pandas](https://pandas.pydata.org/) - Data manipulation
- [OpenPyXL](https://openpyxl.readthedocs.io/) - Excel file handling

---

**Happy analyzing! 📊✨**

