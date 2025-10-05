# TODO - SPSS Prep Tool

Project task list with priorities and status tracking.

---

## ✅ P0 - Must Have (Core Features)

- [x] Basic file upload interface
- [x] Excel file reading with pandas
- [x] Data preview (first 5 rows)
- [x] Detect unique values per column
- [x] Column metadata detection (unique count, missing values)
- [x] Reorder options UI (Up/Down buttons)
- [x] Column configuration cards with expanders
- [x] Encoding type selection (Likert, Nominal, Ignore)
- [x] Start value and direction configuration
- [x] Generate numeric encoding mappings
- [x] Apply encoding to dataframe
- [x] Export encoded Excel file
- [x] Generate SPSS `.sps` syntax file
- [x] GET DATA block generation
- [x] VALUE LABELS block generation
- [x] Preview SPSS syntax in UI
- [x] Download buttons for files
- [x] Auto-updating TODO sidebar checklist
- [x] Variable name sanitization for SPSS
- [x] Multi-response detection and warning
- [x] Unit tests for core functions
- [x] Documentation (README.md)

---

## 🔧 P1 - Should Have (Enhanced Features)

- [x] Likert scale detection heuristic
- [x] VARIABLE LABELS generation (preserve original names)
- [x] Optional SAVE OUTFILE command
- [x] Settings toggles in sidebar
- [x] Reset UI button
- [x] Missing value handling configuration
- [x] Error handling for bad uploads
- [x] Logging for important events
- [ ] Sample input Excel file generation
- [ ] Column type badges (numeric, Likert, etc.)
- [ ] Mapping preview in configuration cards
- [ ] Comprehensive error messages
- [ ] Input validation for all fields
- [ ] Confirmation dialog before reset

---

## 🚀 P2 - Nice to Have (Polish & UX)

- [ ] **Multi-response splitting** - Generate dummy variables for checkbox columns
  - Owner: TBD
  - Complexity: High
  - Notes: Parse comma/semicolon-separated values, create binary dummy columns, add special syntax to .sps

- [ ] **Google Forms API integration** - Direct import from Google Forms
  - Owner: TBD
  - Complexity: Medium
  - Notes: OAuth authentication, form response fetching, real-time sync

- [ ] **Predefined Likert templates** - Quick apply common scales
  - Owner: TBD
  - Complexity: Low
  - Notes: Dropdown with templates like "5-point Likert (Strongly Disagree to Strongly Agree)"

- [ ] **Bulk column operations** - Apply settings to multiple columns at once
  - Owner: TBD
  - Complexity: Medium
  - Notes: Select multiple columns, apply same encoding type/start value/direction

- [ ] **Custom missing value codes** - Allow user to define specific missing codes
  - Owner: TBD
  - Complexity: Low
  - Notes: Text input for missing labels (e.g., "N/A", "Prefer not to answer")

- [ ] **Export configuration JSON** - Save/load encoding configurations
  - Owner: TBD
  - Complexity: Low
  - Notes: JSON serialization of column configs, import on next session

- [ ] **Dark mode theme** - Toggle for dark UI
  - Owner: TBD
  - Complexity: Low
  - Notes: Use Streamlit theming capabilities

- [ ] **Column search/filter** - Search box to filter columns by name
  - Owner: TBD
  - Complexity: Low
  - Notes: Useful for datasets with many columns

- [ ] **Undo/Redo functionality** - Revert configuration changes
  - Owner: TBD
  - Complexity: Medium
  - Notes: Session state history tracking

- [ ] **Statistics summary** - Show descriptive stats per column
  - Owner: TBD
  - Complexity: Low
  - Notes: Mean, median, mode for numeric; frequency distribution for categorical

---

## 🔬 P3 - Advanced Features (Future)

- [ ] **Automatic SPSS execution** - Run SPSS if installed locally
  - Owner: TBD
  - Complexity: High
  - Notes: Detect SPSS installation, execute .sps via command line, requires SPSS license

- [ ] **CSV import support** - Handle .csv files in addition to .xlsx
  - Owner: TBD
  - Complexity: Low
  - Notes: Add CSV upload option, handle encoding detection

- [ ] **Data validation rules** - Define and check data quality rules
  - Owner: TBD
  - Complexity: Medium
  - Notes: Min/max ranges, required fields, pattern matching

- [ ] **Batch processing** - Process multiple files at once
  - Owner: TBD
  - Complexity: Medium
  - Notes: Upload multiple files, apply same config, zip output

- [ ] **Reverse encoding** - Import .sav and decode to labeled Excel
  - Owner: TBD
  - Complexity: High
  - Notes: Parse SPSS .sav files, extract value labels, create decoded spreadsheet

- [ ] **Web deployment** - Deploy to cloud (Streamlit Cloud, Heroku)
  - Owner: TBD
  - Complexity: Medium
  - Notes: Handle file storage, security, user sessions

- [ ] **User authentication** - Multi-user support with saved projects
  - Owner: TBD
  - Complexity: High
  - Notes: Login system, database for user configs, project management

- [ ] **Data transformation pipeline** - Chain multiple operations
  - Owner: TBD
  - Complexity: High
  - Notes: Filter rows, compute new columns, merge datasets

- [ ] **Interactive charts** - Visualize distributions before encoding
  - Owner: TBD
  - Complexity: Medium
  - Notes: Plotly charts for response frequencies

- [ ] **Export to other formats** - Support Stata, R, SAS syntax
  - Owner: TBD
  - Complexity: High
  - Notes: Generate .do, .R, .sas files with appropriate syntax

---

## 🐛 Known Issues

- [ ] **Large file performance** - Files with >100 columns may be slow to configure
  - Priority: P2
  - Workaround: Use column filtering when implemented

- [ ] **Unicode in SPSS syntax** - Some special characters may not render correctly in SPSS
  - Priority: P2
  - Workaround: Avoid special Unicode characters in value labels

- [ ] **Temporary file cleanup** - Generated files stay in system temp directory
  - Priority: P3
  - Workaround: Manually clean temp folder periodically

---

## 📊 Progress Summary

- **P0 (Must Have):** 21/21 complete ✅
- **P1 (Should Have):** 9/15 complete (60%)
- **P2 (Nice to Have):** 0/10 complete (0%)
- **P3 (Advanced):** 0/10 complete (0%)

**Overall Completion:** ~65% of planned features implemented

---

## 🎯 Next Sprint Goals

1. Complete P1 items (column badges, better error handling)
2. Generate comprehensive sample input file
3. Implement multi-response splitting (P2 priority)
4. Add predefined Likert templates
5. Export/import configuration JSON

---

*Last updated: 2025-10-05*

