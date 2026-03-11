# Security Policy

## Overview

OSINTForge is an open-source OSINT (Open Source Intelligence) reconnaissance tool designed for legitimate security research, penetration testing, and cybersecurity purposes. This document outlines our security practices, responsible use guidelines, and vulnerability disclosure process.

## Ethical Usage Guidelines

### Authorized Use Only
- **Only conduct OSINT research on systems/data you own or have explicit written authorization to test**
- Obtain proper legal consent before performing any reconnaissance
- Respect all applicable laws and regulations in your jurisdiction
- Follow your organization's security policies and guidelines

### Prohibited Activities
- ❌ Unauthorized access to computer systems or networks
- ❌ Data theft or intellectual property violation
- ❌ Harassment, stalking, or privacy violations
- ❌ Selling or distributing private information
- ❌ Denial of service attacks
- ❌ Any illegal activities under local, state, or federal law

### Responsible Disclosure
If your OSINT research uncovers a vulnerability:
1. **Do not exploit** the vulnerability beyond what's necessary to confirm it
2. **Document findings** with detailed technical information
3. **Contact vendor privately** before public disclosure
4. **Allow reasonable time** (typically 90 days) for patching
5. **Coordinate disclosure** to minimize harm

## Reporting Security Vulnerabilities

If you discover a security vulnerability in OSINTForge, please report it responsibly:

### Do Not
- ❌ Open a public GitHub issue
- ❌ Share vulnerability details publicly
- ❌ Exploit the vulnerability
- ❌ Test against non-owned systems

### Do
- ✅ Email security details to: [admin@osintintelligence.xyz]
- ✅ Include proof of concept (optional but helpful)
- ✅ Allow reasonable time for response and patching
- ✅ Include your contact information

### Vulnerability Report Template

```
Subject: Security Vulnerability Report - [Brief Description]

Body:
Vulnerability Type: [XSS, RCE, Injection, Authentication, etc.]
Severity: [Critical/High/Medium/Low]
Affected Component: [Module/Core file]
Affected Versions: [1.0.0, etc.]

Description:
[Detailed explanation of vulnerability]

Steps to Reproduce:
1. [Step 1]
2. [Step 2]
3. [Step 3]

impact:
[What could an attacker do with this vulnerability?]

Proof of Concept:
[Code or steps to demonstrate, if applicable]

Remediation:
[Suggested fix, if you have one]

Your Contact Information:
Name: [Your name]
Email: [Your email]
GPG Key: [If you'd like encrypted communication]
```

## Security Best Practices for Users

### API Key Security
```python
# ✅ GOOD: Use environment variables
import os
api_key = os.environ.get('CUSTOM_IP_API_KEY')

# ✅ GOOD: Use configuration file with restrictive permissions
# File: ~/.osintforge/config.json (chmod 600)
# Never commit API keys to git
```

### Git Security
```bash
# ✅ GOOD: Use .gitignore to prevent credential leaks
echo "config.json" >> .gitignore
echo "*.key" >> .gitignore

# ✅ GOOD: Clean git history if keys were accidentally committed
git filter-branch --tree-filter 'rm -f config.json'
```

### Network Security
- Use a VPN when conducting OSINT research on untrusted networks
- Ensure your ISP logs are reviewed (legal requirements vary by locality)
- Consider using a dedicated VM for security research
- Monitor outbound connections for suspicious activity

### Data Protection
```python
# ✅ GOOD: Store sensitive results securely
# Export to encrypted container or password-protected archive
# Keep search history private
# Don't share results with unauthorized parties

# ✅ GOOD: Delete sensitive data when no longer needed
import os
os.remove('sensitive_results.csv')
```

## Code Security

### Input Validation
- All user input is validated before processing
- URLs and IPs are checked for valid format
- Special characters are properly escaped
- SQL injection is prevented (no SQL queries in current version)

### External Dependencies
- Dependencies are regularly audited for vulnerabilities
- Use `pip audit` to check for known vulnerabilities:
  ```bash
  pip install pip-audit
  pip-audit
  ```

### Regular Updates
```bash
# Check for updates
pip list --outdated

# Update dependencies
pip install --upgrade -r requirements.txt

# Audit dependencies
pip-audit --fix
```

## Infrastructure Security

### Official Distribution
- Only download OSINTForge from official GitHub repository
- Verify releases with GPG signatures (when available)
- Check SHA256 hashes for downloaded files

### Malware Prevention
OSINTForge is:
- ✅ Free and open source (code available for review)
- ✅ No external phone-home or telemetry
- ✅ No cryptocurrency mining
- ✅ No credential harvesting
- ✅ No unauthorized data collection

If you're concerned about a false positive from Windows Defender:
```bash
# This is normal for unsigned executables
# Windows Defender flags them as "Unknown Software"
# You can safely ignore this warning

# To create a signed version:
# 1. Obtain a code signing certificate
# 2. Use signtool.exe (Windows SDK)
# 3. Command: signtool sign /f certificate.pfx /p password app.exe
```

## Privacy Policy

### What OSINTForge Collects
- ✅ None - All operations are local
- ✅ No telemetry data
- ✅ No usage statistics
- ✅ No crash reporting
- ✅ No analytics

### What You Should Know
- Results are stored locally in `~/.osintforge/`
- API calls to external services (IP-API, HackerTarget, suicixde.com) may log your IP
- Custom API (suicixde.com) respects privacy per its terms
- Keep your API keys private and never share them

## Compliance

### Data Protection Laws
OSINTForge users are responsible for complying with:
- GDPR (EU General Data Protection Regulation)
- CCPA (California Consumer Privacy Act)
- HIPAA (Health Insurance Portability and Accountability Act)
- Local data protection regulations

### Legal Considerations
- Authorized penetration testing requires written authorization
- Some countries restrict certain OSINT techniques
- Always consult with legal counsel before conducting OSINT
- Respect intellectual property rights

## Security Checklist

Before using OSINTForge:
- [ ] Read this entire security policy
- [ ] Understand applicable laws in your jurisdiction  
- [ ] Obtain proper authorization for targets
- [ ] Protect your API keys and configuration
- [ ] Use a VPN for sensitive research
- [ ] Keep dependencies updated
- [ ] Review [CONTRIBUTING.md](CONTRIBUTING.md) if submitting code
- [ ] Accept responsibility for your actions

## Common Security Questions

### Q: Is OSINTForge legal?
**A:** The tool itself is legal, but how you use it must be. Always get permission before researching targets.

### Q: Can I run this on other people's networks?
**A:** Only if you have explicit written authorization. Unauthorized network access is illegal.

### Q: Is my data encrypted?
**A:** Data is stored locally in `~/.osintforge/`. Use full disk encryption for additional protection.

### Q: Can I use this for malicious purposes?
**A:** No. Misusing this tool for illegal activities is your responsibility and illegal.

### Q: Should I trust this tool?
**A:** Verify the code yourself. It's open source on GitHub. Review dependencies and security practices.

## Support & Contact

### Security Issues
- Email: [admin@osintintelligence.xyz]
- Do not open public issues for security vulnerabilities

### General Questions
- GitHub Issues: [GitHub Repository Issues](https://github.com/yourusername/osintforge/issues)
- Discussions: [GitHub Discussions](https://github.com/yourusername/osintforge/discussions)

### Legal Concerns
- Consult with legal counsel in your jurisdiction
- Contact GitHub's Trust & Safety team if needed

## Disclaimer

OSINTForge is provided "as-is" without any warranty. Users assume full responsibility for:
- Adequate training and knowledge
- Proper authorization before using the tool
- Compliance with all applicable laws
- Ethical use in security research
- Consequences of misuse

The developers and contributors are not liable for:
- Unauthorized access to systems
- Privacy violations
- Intellectual property infringement
- Data loss or corruption
- Any damages resulting from misuse

## Version History

- **1.0.0** (2024-01-XX) - Initial release with security guidelines

## Acknowledgments

Thank you to the security research community for responsible disclosure practices and ethical guidelines.

---

**By using OSINTForge, you agree to:**
1. Use this tool only for authorized purposes
2. Comply with all applicable laws
3. Respect privacy and data protection rights
4. Follow responsible disclosure practices
5. Accept full responsibility for your actions

**Remember: With great power comes great responsibility. Use ethically and legally.** 🛡️

