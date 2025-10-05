# 🚀 QUICKSTART GUIDE

Get started with the SPSS Prep Tool in 3 minutes!

---

## ⚡ Installation & Launch

```bash
# 1. Install dependencies (if not already done)
pip install -r requirements.txt

# 2. Launch the app
streamlit run app.py
```

Your browser will open automatically to `http://localhost:8501`

---

## 📝 Quick Demo with Sample Data

1. **Launch the app** (see above)

2. **Upload the sample file:**
   - Click "Browse files"
   - Select `sample_input.xlsx` from this directory
   - See the preview of 6 survey responses

3. **Configure a column (Example: Satisfaction):**
   - Expand "How satisfied are you with our service?"
   - See it's detected as Likert-scale (6 unique values)
   - The order is already set by frequency
   - **Try reordering:** Click ↑ or ↓ to move options
   - Set: Encoding Type = **Likert**, Start Value = **1**, Direction = **Ascending**
   - Preview shows: Very Satisfied → 1, Satisfied → 2, etc.

4. **Configure more columns:**
   - "How often do you use our product?" → **Likert** (frequency scale)
   - "Your age group" → **Nominal** (no inherent order)
   - "Would you recommend us?" → **Likert** or **Nominal**
   - "Additional comments" → **Ignore** (free text)

5. **Generate files:**
   - Click **"🚀 Apply Encoding & Generate Files"**
   - Wait 2-3 seconds

6. **Download & preview:**
   - See encoded data preview (text → numbers)
   - See SPSS syntax preview (`.sps` script)
   - Download both files using the buttons

7. **Use in SPSS:**
   - Open SPSS Statistics
   - File → Open → Syntax
   - Select the downloaded `.sps` file
   - Run → All (or Ctrl+A, Ctrl+R)
   - Your encoded data is now imported with value labels!

---

## 💡 Key Features to Try

### ↕️ Reordering Options
- Use ↑ ↓ buttons to arrange response order
- Order determines numeric codes
- First item → lowest code (Ascending) or highest code (Descending)

### 🔢 Direction Control
- **Ascending:** "Low" → 1, "Medium" → 2, "High" → 3
- **Descending:** "Low" → 3, "Medium" → 2, "High" → 1
- Useful for reverse-coded items

### 🏷️ Variable Name Sanitization
- Automatically converts "How satisfied?" → "How_satisfied"
- Ensures SPSS compatibility (no spaces, special chars)
- Edit the sanitized name if needed

### ✅ Progress Checklist
- Watch the sidebar TODO list update automatically
- Green checkmarks show completed steps
- Helps you track progress

---

## 🎯 Common Use Cases

### Use Case 1: 5-Point Likert Scale
```
Original: Strongly Disagree, Disagree, Neutral, Agree, Strongly Agree
Setup: Likert, Start=1, Ascending
Result: 1, 2, 3, 4, 5
```

### Use Case 2: Reverse-Coded Item
```
Original: Strongly Agree, Agree, Neutral, Disagree, Strongly Disagree
Setup: Likert, Start=1, Descending
Result: 5, 4, 3, 2, 1 (Strongly Agree=5)
```

### Use Case 3: Nominal Categories
```
Original: Red, Blue, Green, Yellow
Setup: Nominal, Start=1, Ascending
Result: Arbitrary numeric codes (1, 2, 3, 4)
Note: Order doesn't matter for nominal data
```

---

## ⚙️ Settings Explained

**Sidebar Settings:**

| Setting | Default | Purpose |
|---------|---------|---------|
| Include SAVE OUTFILE | Off | Add command to create .sav file |
| Write .sps to same folder | On | Place syntax next to Excel file |
| Sanitize variable names | On | Convert names to SPSS format |

---

## 🐛 Troubleshooting

### App won't start
```bash
# Make sure Streamlit is installed
pip install streamlit

# Try again
streamlit run app.py
```

### "No module named X"
```bash
# Reinstall all dependencies
pip install -r requirements.txt
```

### Can't upload Excel file
- Make sure file is `.xlsx` format (not `.xls` or `.csv`)
- File should have column headers in first row
- Close the file in Excel if it's open

### SPSS won't import
- Check the file path in the `.sps` is correct
- Make sure the encoded Excel file exists at that location
- Try opening the Excel file first to verify it's readable

---

## 📚 Next Steps

- **Read full documentation:** Check `README.md` for detailed features
- **Review decisions:** See `CHANGELOG` for implementation choices  
- **Plan improvements:** Check `TODO.md` for future features
- **Run tests:** Execute `pytest tests/ -v` to verify installation

---

## 🎉 You're Ready!

The SPSS Prep Tool is now set up and working. Upload your own Google Forms export and start encoding!

**Need help?** Check the tooltips (ℹ️) in the app or read the full README.md

---

*Happy analyzing! 📊*

