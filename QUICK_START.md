# Quick Start Guide - OSINTForge

Get up and running with OSINTForge in 5 minutes!

## 📦 Installation

### Windows
```powershell
# Clone the repository
git clone https://github.com/yourusername/osintforge.git
cd osintforge

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Linux/Mac
```bash
# Clone the repository
git clone https://github.com/yourusername/osintforge.git
cd osintforge

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## 🚀 First Run

When you start OSINTForge:

1. **See the banner** - Professional styled ASCII art welcome screen
2. **Select a module** - Choose from 13 OSINT tools (or settings/history)
3. **Enter target** - Input the IP, domain, email, etc.
4. **View results** - Beautifully formatted tables with key information

```
┌──────────────────────────────────────────────┐
│                  OSINTFORGE                  │
│          Open Source Intelligence Tool       │
│                  v1.0.0                      │
└──────────────────────────────────────────────┘

Select a module (1-17): 1

Enter IP address: 1.1.1.1
🔍 Processing...

┌────────────────┬────────────────────────┐
│  Field         │  Value                 │
├────────────────┼────────────────────────┤
│  IP Address    │  1.1.1.1               │
│  Country       │  United States         │
│  City          │  Los Angeles, CA       │
│  Organization  │  Cloudflare, Inc.      │
└────────────────┴────────────────────────┘
```

## 🎯 Common Tasks

### 1. Look Up an IP Address
```
1. Start: python main.py
2. Select: 1 (IP Lookup)
3. Enter: 8.8.8.8
4. View: Location, organization, VPN status
```

### 2. Check Email Validity
```
1. Start: python main.py
2. Select: 2 (Email Lookup)
3. Enter: test@example.com
4. View: Valid/Invalid, disposable check
```

### 3. Enumerate DNS Records
```
1. Start: python main.py
2. Select: 3 (DNS Lookup)
3. Enter: example.com
4. View: A, MX, NS, TXT records
```

### 4. Scan Ports
```
1. Start: python main.py
2. Select: 8 (Port Scanner)
3. Enter: example.com
4. View: Open ports and services
```

### 5. Find Subdomains
```
1. Start: python main.py
2. Select: 7 (Subdomain Enumeration)
3. Enter: example.com
4. View: Discovered subdomains with progress
```

## ⚙️ Configuration

### Change Color Theme

```
1. Main menu: Select 16 (Settings)
2. Choose: 1 (Manage Themes)
3. Select from:
   - 0: Default Cybersecurity (Cyan/Magenta)
   - 1: Dark Terminal (Dark blue/Green)
   - 2: Minimalist (Simple black/white)
   - 3: Hacker Green (Classic green)
```

### Set API Key

```
1. Main menu: Select 16 (Settings)
2. Choose: 4 (Manage API Keys)
3. Enter key for custom IP API
4. Settings save automatically
```

### Export Results

Results are automatically added to history. To export:

```
1. Any module runs a search
2. Select: 15 (Export) after search
3. Choose format: JSON or CSV
4. File saved to current directory with timestamp
```

### View Search History

```
1. Main menu: Select 14 (Search History)
2. View all your previous searches
3. Can mark important ones as favorites
```

## 📊 Module Reference

| # | Module | Purpose |
|---|--------|---------|
| 1 | IP Lookup | Geolocation, VPN detection, hosting info |
| 2 | Email Lookup | Validation, disposable domain check |
| 3 | DNS Lookup | A, MX, NS, TXT, CNAME, SOA records |
| 4 | Phone Lookup | Validation, country detection |
| 5 | SSL Lookup | Certificate details, validity date |
| 6 | Website Info | Headers, security check, server info |
| 7 | Subdomain Enum | Pattern-based subdomain discovery |
| 8 | Port Scanner | 19 common service ports |
| 9 | Hash Lookup | Hash type identification |
| 10 | Geolocation | Multi-layer geolocation data |
| 11 | Username Search | Username availability check |
| 12 | Domain Lookup | WHOIS, registration info |
| 13 | Reverse DNS | IP to hostname resolution |

## 🔑 Menu Options

- **1-13**: OSINT Modules (listed above)
- **14**: Search History (view previous searches)
- **15**: Export (save results as JSON/CSV)
- **16**: Settings (themes, API keys, timeouts)
- **17**: Exit (quit program)

## 🎨 Color Themes

OSINTForge ships with 4 pre-configured themes:

### Default Cybersecurity 🔵
- Bright cyan and magenta colors
- Professional security research feel
- High contrast for readability

### Dark Terminal 🟢
- Dark blue and green palette
- Low eye strain for long sessions
- Classic terminal aesthetic

### Minimalist ⚪
- Black and white only
- No color distraction
- Maximum compatibility

### Hacker Green 💚
- Classic green monochrome
- Nostalgic retro feel
- Terminal-style appearance

Change anytime in Settings → Manage Themes

## 📁 File Locations

OSINTForge stores data in `~/.osintforge/`:

```
~/.osintforge/
├── settings.json          # Your configuration and preferences
├── search_history.json    # All your searches
├── favorites.json         # Marked favorite searches
└── exports/               # Exported results
```

To reset everything:
```bash
rm -rf ~/.osintforge
# OSINTForge recreates with defaults on next run
```

## 🐛 Troubleshooting

### "Module not found" error
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### API key not working
```
1. Settings → Manage API Keys
2. Clear and re-enter your key
3. Key saves to ~/.osintforge/settings.json
```

### Results not showing
```
1. Check internet connection
2. Verify target format (e.g., valid domain)
3. Some modules may have rate limits
4. Try a different module
```

### Timeout error
```
Settings → Manage Timeout
 Default: 30 seconds
Increase if getting regular timeouts
```

### Windows Defender warning
This is normal for unsigned executables. Click "More info" → "Run anyway"

## 📚 More Information

- **README.md** - Full documentation and features
- **CONTRIBUTING.md** - How to contribute to the project
- **SECURITY.md** - Security guidelines and responsible use
- **CHANGELOG.md** - Version history and roadmap

## ✨ Pro Tips

1. **Mark Favorites** - After search, choose to save to favorites for quick reference
2. **Use Export** - Save findings as CSV for spreadsheet analysis
3. **Change Themes** - Different themes help reduce eye strain
4. **Check History** - See previous research without re-running
5. **Custom API** - Set your API key for better IP geolocation accuracy

## 🚨 Important Reminders

⚠️ **Always obtain authorization before researching:**
- Targets you don't own
- Systems you don't have permission for
- Private information

✅ **Use responsibly for:**
- Authorized penetration testing
- Personal security research
- Educational purposes
- Legitimate threat intelligence

## 🤝 Need Help?

1. Check README.md for detailed documentation
2. Review CONTRIBUTING.md for development questions
3. Open GitHub issue for bug reports
4. Ask in GitHub Discussions for questions

## 🎓 Learning Path

**Beginner:**
1. Try IP Lookup (1) with simple IPs (8.8.8.8, 1.1.1.1)
2. Try Email Lookup (2) with test emails
3. Explore DNS Lookup (3) with known domains

**Intermediate:**
1. Port Scanner (8) on known targets
2. Subdomain Enumeration (7) on target domains
3. SSL Lookup (5) for certificate analysis
4. Combine multiple modules for deeper research

**Advanced:**
1. Automate repeated searches with history
2. Export results for analysis
3. Develop new modules (see CONTRIBUTING.md)
4. Integrate with other tools

---

## Ready to Get Started?

```bash
python main.py
```

That's it! Start with module 1 (IP Lookup) and explore from there.

**Happy hunting!** 🔍🎯
