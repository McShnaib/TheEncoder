# Security Policy

## Supported Versions

We actively support the following versions of SPSS Prep Tool with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.2.x   | ✅                |
| 1.1.x   | ✅                |
| 1.0.x   | ❌ (End of Life)  |
| < 1.0   | ❌                |

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you believe you have found a security vulnerability in SPSS Prep Tool, please report it to us responsibly.

### 🔒 Private Reporting

**DO NOT** create public GitHub issues for security vulnerabilities.

Instead, please:

1. **Email us privately** at: [INSERT SECURITY EMAIL]
2. **Include the following information:**
   - Description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact assessment
   - Suggested fix (if you have one)

### 📋 What to Include in Your Report

Please provide as much information as possible to help us understand and fix the issue:

- **Vulnerability type** (e.g., XSS, SQL injection, file upload, etc.)
- **Affected component** (e.g., file upload, data processing, SPSS generation)
- **Attack vector** (local, remote, authenticated, etc.)
- **Steps to reproduce** (detailed instructions)
- **Proof of concept** (code, screenshots, etc.)
- **Impact assessment** (what could an attacker achieve?)
- **Affected versions** (if known)

### ⏱️ Response Timeline

- **Initial response**: Within 48 hours
- **Assessment completion**: Within 7 days
- **Fix timeline**: Depends on severity (see below)

### 🚨 Severity Levels

#### Critical (Fix within 24-48 hours)
- Remote code execution
- Data breach or unauthorized data access
- Authentication bypass

#### High (Fix within 1 week)
- Local code execution
- Privilege escalation
- Significant data exposure

#### Medium (Fix within 2 weeks)
- Cross-site scripting (XSS)
- Cross-site request forgery (CSRF)
- Information disclosure

#### Low (Fix in next release)
- Minor information leaks
- Non-security-impacting bugs

## 🛡️ Security Measures

### Current Security Features

1. **Input Validation**
   - File type restrictions (only .xlsx)
   - File size limits
   - Content sanitization

2. **Data Processing**
   - No external network calls
   - Local file processing only
   - Temporary file cleanup

3. **Dependencies**
   - Regular security updates
   - Minimal dependency footprint
   - Trusted packages only

### Known Security Considerations

1. **File Upload Security**
   - Only processes Excel files
   - No macro execution
   - Limited to safe file operations

2. **Data Privacy**
   - No data is sent to external servers
   - All processing happens locally
   - Temporary files are cleaned up

3. **Output Files**
   - Generated files contain no executable code
   - SPSS syntax is text-only
   - No embedded macros or scripts

## 🏗️ Security Best Practices for Users

### For End Users

1. **Keep Updated**
   ```bash
   pip install --upgrade spss-prep-tool
   ```

2. **Verify Downloads**
   - Only download from official sources
   - Check file hashes if available

3. **Secure Environment**
   - Run in isolated environments when possible
   - Don't upload sensitive data unnecessarily
   - Review generated SPSS syntax before execution

4. **Data Handling**
   - Remove personal identifiers before processing
   - Use secure file storage
   - Delete temporary files after use

### For Developers

1. **Dependency Management**
   ```bash
   # Check for vulnerabilities
   safety check
   
   # Update dependencies
   pip-audit
   ```

2. **Code Security**
   ```bash
   # Run security linter
   bandit -r src/
   
   # Check for secrets
   detect-secrets scan
   ```

3. **Testing**
   - Include security tests in test suite
   - Test with malicious inputs
   - Validate all user inputs

## 🔍 Security Auditing

### Automated Checks

We use the following tools in our CI/CD pipeline:

- **Safety**: Python package vulnerability scanning
- **Bandit**: Static security analysis
- **CodeQL**: Semantic code analysis
- **Dependabot**: Dependency vulnerability alerts

### Manual Reviews

- Security review for all pull requests
- Regular dependency audits
- Periodic security assessments

## 📜 Vulnerability Disclosure Policy

### Our Commitment

- We will investigate all legitimate reports
- We will keep you updated on our progress
- We will credit you in our security advisory (if desired)
- We will not pursue legal action for good faith security research

### Responsible Disclosure

Please:
- Give us reasonable time to fix the issue before public disclosure
- Don't access or modify data that doesn't belong to you
- Don't perform DoS attacks or spam
- Don't violate any laws or regulations

### Public Disclosure

After a fix is released:
- We will publish a security advisory
- We will credit the reporter (unless they prefer anonymity)
- We will document the fix in our changelog

## 🏆 Security Hall of Fame

We recognize security researchers who help improve our security:

*[No vulnerabilities reported yet - be the first!]*

## 📚 Security Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.org/dev/security/)
- [Streamlit Security Guidelines](https://docs.streamlit.io/library/advanced-features/security)

## 📞 Contact Information

- **Security Email**: [INSERT SECURITY EMAIL]
- **General Issues**: [GitHub Issues](https://github.com/your-org/spss-prep-tool/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/spss-prep-tool/discussions)

---

*Last updated: October 2025*
