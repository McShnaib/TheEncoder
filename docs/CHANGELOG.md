# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Complete open-source project structure
- MIT License for open distribution
- Comprehensive contribution guidelines (CONTRIBUTING.md)
- Community Code of Conduct (CODE_OF_CONDUCT.md)
- GitHub Actions for CI/CD automation
- Pre-commit hooks for code quality
- Security policy and guidelines (SECURITY.md)
- Detailed installation guide (INSTALL.md)
- Proper Python packaging (pyproject.toml)
- Professional README with badges and community info

### Changed
- Reorganized project structure with proper src/ layout
- Enhanced README with open-source standards
- Improved documentation organization
- Updated development workflow

### Removed
- Duplicate files from root directory
- Build artifacts from version control
- Legacy build scripts

## [1.2.0] - 2025-10-05 (Feature Update - Arabic Variable Names)

### Changed
- Variable names now preserve Arabic text instead of converting to var1, var2, etc.
- Updated `sanitize_variable_name()` to keep Unicode characters (Arabic, Chinese, etc.)
- SPSS fully supports Unicode in variable names - no need to replace them!

### Added
- Arabic column names: "السؤال الأول" → "السؤال_الأول" (not "var1")
- English columns: "Age Group" → "Age_Group" (no change)
- Mixed: "Question السؤال" → "Question_السؤال" (preserved)
- Handles duplicates by adding _1, _2, etc. if needed
- Added 8 new unit tests - all 33 tests passing

### Technical Details
- Spaces and special punctuation become underscores
- More intuitive and readable in SPSS!

## [1.1.2] - 2025-10-04 (Critical Bug Fix - SPSS Import)

### Fixed
- Excel files now import correctly into SPSS without manual intervention
- GET DATA Error 2052 resolved with proper directory setup

### Changed
- Changed Excel engine from openpyxl to xlsxwriter for better SPSS compatibility
- Added CD command to .sps files to set working directory
- Added clear step-by-step instructions in both app UI and .sps files

### Technical Details
- Excel files no longer need to be manually opened/resaved before SPSS import
- See `BUGFIX_v1.1.2_SPSS_Import.md` for complete details

## [1.1.1] - 2025-10-03 (Critical Bug Fix - Arabic Support)

### Fixed
- SPSS syntax errors caused by invisible Unicode bidirectional formatting characters
- Arabic (and other RTL languages) now work perfectly in SPSS

### Added
- `strip_bidi_characters()` function to remove RTL/LTR marks and embeddings
- Applied to sheet names, variable names, and all text in VALUE LABELS
- Added 6 new unit tests - all 26 tests passing

### Impact
- Makes Arabic surveys fully functional (was completely broken)
- See `BUGFIX_v1.1.1_BidiCharacters.md` for technical details

## [1.1.0] - 2025-10-02 (Major Feature Update)

### Added
- SPSS terminology alignment and Arabic language support improvements
- VARIABLE LEVEL command to set measure types automatically
- Unique variable name generation for Arabic columns (var1, var2, etc.)
- UTF-8 BOM encoding for Arabic text display
- Relative paths in .sps files for easier portability

### Changed
- Changed UI from "Likert/Nominal" to SPSS "Ordinal/Nominal/Scale"

### Technical Details
- See `UPDATES_v1.1.0.md` for complete details

## [1.0.1] - 2025-10-01 (Bug Fix)

### Fixed
- VALUE LABELS and VARIABLE LABELS syntax now properly includes forward slashes (`/`) between variables
- SPSS requires forward slashes to separate variables in multi-variable label blocks
- Each variable line now ends with ` /` except the last which ends with `.`

### Acknowledgments
- Thanks to user testing for catching this issue!

## [1.0.0] - 2025-09-30 (Initial Release)

### Added
- Core Streamlit web application
- Excel file upload and preview functionality
- Automatic column detection and classification
- Interactive column configuration with reordering
- Support for Ordinal (Likert), Nominal, and Scale variable types
- SPSS syntax generation with VALUE LABELS and VARIABLE LABELS
- Encoded Excel file generation
- Variable name sanitization for SPSS compatibility
- Multi-response detection and warnings
- Comprehensive test suite (20+ tests)
- Complete documentation suite

### Features
- 📤 Upload Excel files (Google Forms exports)
- 🔍 Automatic detection of unique values per column
- 🎯 Smart heuristics for Likert scale detection
- ↕️ Reorder options with Up/Down buttons
- 🔢 Flexible encoding (start values and direction)
- ✅ Interactive TODO checklist in sidebar
- 📊 Multiple encoding types (Ordinal, Nominal, Scale, Ignore)
- 🏷️ Variable name sanitization for SPSS compatibility
- ⚠️ Multi-response detection and warnings
- 📜 Complete SPSS syntax generation (.sps files)
- 💾 Download both encoded Excel and SPSS syntax files

### Technical Implementation
- Built with Streamlit 1.28+
- Pandas 2.0+ for data manipulation
- OpenPyXL 3.1+ for Excel handling
- Comprehensive error handling and logging
- Type hints throughout codebase
- 65%+ test coverage

---

## Development Guidelines

### Version Numbering
This project follows [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions
- **PATCH** version for backwards-compatible bug fixes

### Release Process
1. Update version numbers in `pyproject.toml` and `src/spss_prep/__init__.py`
2. Update this CHANGELOG.md with new features, changes, and fixes
3. Create and merge pull request
4. Tag release: `git tag -a v1.2.1 -m "Release version 1.2.1"`
5. Push tag: `git push origin v1.2.1`
6. GitHub Actions will automatically create release

### Change Categories
- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for any bug fixes
- **Security** for vulnerability fixes

---

*For the complete project history, see individual commit messages and pull requests.*
