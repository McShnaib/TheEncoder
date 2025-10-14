# Contributing to SPSS Prep Tool

First off, thank you for considering contributing to SPSS Prep Tool! 🎉 It's people like you that make this tool better for survey researchers and data analysts worldwide.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Pull Request Process](#pull-request-process)
- [Testing](#testing)
- [Documentation](#documentation)
- [Reporting Issues](#reporting-issues)
- [Feature Requests](#feature-requests)
- [Community](#community)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Basic knowledge of Python and Streamlit
- Understanding of SPSS data formats (helpful but not required)

### Development Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/your-username/spss-prep-tool.git
   cd spss-prep-tool
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If available
   ```

4. **Run the application:**
   ```bash
   streamlit run spss_prep/app.py
   ```

5. **Run tests:**
   ```bash
   pytest tests/ -v
   ```

## 🤝 How to Contribute

### Types of Contributions

We welcome many types of contributions:

- 🐛 **Bug fixes**
- ✨ **New features** (see our [TODO.md](TODO.md) for ideas)
- 📚 **Documentation improvements**
- 🧪 **Tests** (we can always use more!)
- 🌐 **Translations** (especially for non-English surveys)
- 💡 **Feature suggestions**
- 🔧 **Code refactoring**

### Contribution Workflow

1. **Check existing issues** - Look for existing issues or feature requests
2. **Create an issue** - If none exists, create one describing what you plan to work on
3. **Fork the repo** - Create your own fork
4. **Create a branch** - Use a descriptive branch name
5. **Make changes** - Write your code following our guidelines
6. **Add tests** - Ensure your changes are tested
7. **Update documentation** - Update relevant docs
8. **Submit PR** - Create a pull request with clear description

### Branch Naming

Use descriptive branch names:
- `feature/multi-response-splitting`
- `fix/unicode-handling`
- `docs/installation-guide`
- `refactor/column-detection`

### Commit Messages

Write clear commit messages:
- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests liberally

Example:
```
Add multi-response column splitting

- Implement parsing of comma-separated values
- Generate dummy variables for each response
- Add MRSETS syntax to SPSS output
- Fixes #15
```

## 🔧 Pull Request Process

### Before Submitting

- [ ] Code follows the project style (run `black` and `flake8` if available)
- [ ] All tests pass (`pytest tests/`)
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated (if applicable)

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other (please describe)

## Testing
- [ ] Tests pass locally
- [ ] Added new tests for functionality
- [ ] Manual testing completed

## Screenshots/Examples
(If applicable)

## Related Issues
Closes #123
```

### Review Process

1. All PRs require at least one review
2. CI checks must pass
3. Changes should be backwards compatible (unless major version)
4. Breaking changes need detailed migration guide

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_encoding.py -v

# Run with coverage
pytest tests/ --cov=spss_prep --cov-report=html
```

### Writing Tests

- Place tests in `tests/` directory
- Name test files `test_*.py`
- Use descriptive test function names
- Test both success and failure cases
- Mock external dependencies (file I/O, etc.)

Example:
```python
def test_sanitize_variable_name_with_arabic():
    """Test that Arabic characters are preserved in variable names."""
    result = sanitize_variable_name("السؤال الأول")
    assert result == "السؤال_الأول"
```

## 📚 Documentation

### Types of Documentation

- **Code documentation**: Docstrings, inline comments
- **User documentation**: README.md, QUICKSTART.md
- **Developer documentation**: This file, architectural decisions
- **API documentation**: Function/class documentation

### Documentation Standards

- Use clear, concise language
- Include examples where helpful
- Update documentation with code changes
- Use proper Markdown formatting
- Include screenshots for UI changes

## 🐛 Reporting Issues

### Bug Reports

Use our bug report template and include:

- **Description**: Clear description of the bug
- **Steps to reproduce**: Minimal steps to trigger the issue
- **Expected behavior**: What you expected to happen
- **Actual behavior**: What actually happened
- **Environment**: OS, Python version, package versions
- **Sample data**: If applicable (remove sensitive data)

### Security Issues

For security vulnerabilities, please email the maintainers directly rather than opening a public issue.

## 💡 Feature Requests

We love feature ideas! Before requesting:

1. Check if it's already in our [TODO.md](TODO.md)
2. Search existing issues
3. Consider if it fits the project's scope

Include in your request:
- **Problem**: What problem does this solve?
- **Solution**: Your proposed solution
- **Alternatives**: Other solutions you considered
- **Use case**: Real-world scenario where this helps

## 🏗️ Architecture & Design

### Project Structure

```
spss-prep-tool/
├── spss_prep/           # Main package
│   ├── __init__.py
│   ├── app.py           # Streamlit application
│   ├── encoder.py       # Data encoding logic
│   ├── sps_generator.py # SPSS syntax generation
│   └── utils.py         # Helper functions
├── tests/               # Test suite
├── docs/                # Documentation
├── examples/            # Example files
└── scripts/             # Utility scripts
```

### Design Principles

- **User-first**: Prioritize user experience for researchers
- **Simplicity**: Keep the interface intuitive
- **Reliability**: Robust error handling and validation
- **Extensibility**: Design for future features
- **Performance**: Handle large datasets efficiently

### Key Components

1. **Column Detection** (`encoder.py`): Analyzes uploaded data
2. **Configuration UI** (`app.py`): Interactive column setup
3. **Encoding Engine** (`encoder.py`): Converts values to numeric codes
4. **SPSS Generator** (`sps_generator.py`): Creates `.sps` syntax files

## 🌟 Recognition

Contributors will be:
- Listed in project README
- Credited in release notes
- Invited to join contributor discussions

## 📞 Community

- **Issues**: GitHub Issues for bugs and features
- **Discussions**: GitHub Discussions for questions
- **Email**: Contact maintainers for sensitive issues

## 📝 Development Notes

### Code Style

We follow PEP 8 with some modifications:
- Maximum line length: 88 characters (Black default)
- Use type hints where possible
- Docstrings for all public functions
- Import sorting with `isort`

### Performance Considerations

- Profile code with large datasets (1000+ rows/columns)
- Use efficient pandas operations
- Minimize Streamlit reruns
- Cache expensive computations

### Internationalization

- Design for non-English surveys from the start
- Use Unicode-safe string operations
- Test with Arabic, Chinese, and other non-Latin scripts
- Consider right-to-left text rendering

## 🎉 Thank You!

Every contribution matters, whether it's:
- Fixing a typo
- Adding a major feature  
- Improving documentation
- Reporting a bug
- Suggesting improvements

Thank you for making SPSS Prep Tool better! 🙏

---

*Last updated: October 2025*
