# OSINTForge 🔍

**A Professional Multi-Purpose OSINT Intelligence Framework**

OSINTForge is a powerful, modular Python CLI tool for Open Source Intelligence (OSINT) gathering. It provides a comprehensive suite of reconnaissance modules designed for cybersecurity professionals, investigators, and researchers.

![Python Version](https://img.shields.io/badge/python-3.7+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Active-brightgreen)

## ✨ Features

- **🎨 Professional Colored CLI Interface** - Rich terminal UI with theme support
- **🔄 13+ OSINT Modules** - Comprehensive intelligence gathering tools
- **🎭 4 Built-in Themes** - Customize the visual experience
- **💾 Search History & Favorites** - Track and save your inquiries
- **📊 Export Results** - Save findings in JSON or CSV format
- **⚙️ Settings Management** - Configure timeouts, themes, and API keys
- **📱 Modular Architecture** - Easy to extend with new modules
- **🔒 Local Data Storage** - All data stored securely in user home directory

## 📦 OSINT Modules

### Intelligence Gathering
- **IP Intelligence Lookup** - Comprehensive IP geolocation and analysis
- **Domain Intelligence** - WHOIS data and DNS resolution
- **Username Search** - Cross-platform username reconnaissance
- **Reverse DNS Lookup** - Hostname resolution

### Advanced Lookups
- **Email Validation** - Email verification and analysis
- **DNS Records** - A, AAAA, MX, NS, TXT, CNAME, SOA lookups
- **Phone Analysis** - Phone number validation and country detection
- **SSL Certificates** - Certificate inspection and expiry tracking

### Network & Infrastructure
- **Website Information** - Header analysis and security checks
- **Subdomain Enumeration** - Discover subdomains using pattern matching
- **Port Scanner** - Scan common ports (19 services)
- **Hash Lookup** - Hash type identification and analysis

### Data Analysis
- **Geolocation** - IP location with coordinates and maps
- **Search History** - View and manage recent searches
- **Favorites** - Save frequently used queries

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/xdrew87/osintforge.git
cd osintforge

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`:
  - `rich` - Colored CLI interface
  - `requests` - HTTP requests
  - `dnspython` - DNS operations
  - `email-validator` - Email validation
  - `PyYAML` - Configuration handling

## 💻 Usage

### Starting the Application

```bash
python main.py
```

You'll be greeted with a professional banner and main menu showing all available modules.

### Main Menu Options

```
🔍 OSINT MODULES
#    Module Name              Category
1    IP Intelligence         IP Analysis
2    Domain Intelligence     Domain Analysis
3    Username OSINT          User Profiling
4    Reverse DNS            Network Mapping
5    Email Lookup           Account Analysis
6    DNS Records            Domain Analysis
7    Phone Lookup           Contact Verify
8    SSL Certificate        Security Check
9    Website Information    Web Analysis
10   Subdomain Enum         Infrastructure
11   Port Scanner           Service Discovery
12   Hash Lookup            Data Verification
13   Geolocation            Location Mapping
14   Search History         Data Management
15   Favorites              Data Management
16   ⚙ Settings             Configuration
17   ⏻ Exit                 System
```

### Example Workflow

1. Run `python main.py`
2. Select module (e.g., `1` for IP Intelligence)
3. Enter target information
4. Review results in formatted table
5. Results automatically saved to history
6. Export results from settings if needed

## ⚙️ Configuration

### Settings Menu

Access Settings (Option 16) to:

- **Change Theme** - Switch between 4 color schemes:
  - Default Cybersecurity (Magenta/Cyan/Green)
  - Dark Terminal (Bright colors)
  - Minimalist (Monochrome)
  - Hacker Green (Classic terminal)

- **Set Timeout** - Configure API request timeout (1-300 seconds)

- **Export Format** - Choose JSON or CSV output

- **API Keys** - Store credentials for:
  - VirusTotal
  - Shodan
  - IPQualityScore

### Data Storage

All user data is stored in:
- **Windows**: `~/.osintforge/`
- **Linux/Mac**: `~/.osintforge/`

Files created:
- `settings.json` - User preferences
- `search_history.json` - Recent queries
- `favorites.json` - Saved items
- `exports/` - Exported results

## 🔌 API Information

### Custom IP API

This tool uses a custom IP geolocation API endpoint:

```
https://suicixde.com/api/geoip/
```

**Features:**
- Fast IP geolocation lookups
- VPN/Proxy detection
- Hosting provider identification
- Detailed ISP information
- No API key required

**Response includes:**
- IP address and hostname
- Country, region, city
- Latitude/longitude
- ISP and organization
- VPN/Proxy/Hosting flags
- Connection type

### External Services

- **HackerTarget** - WHOIS lookups
- **ip-api.com** - Enhanced geolocation
- **DNS Resolution** - Standard system DNS

## 🎨 Theme System

### Built-in Themes

**Default Cybersecurity**
- Banner: Magenta
- Menu: Cyan
- Results: Green
- Errors: Red

**Dark Terminal**
- Banner: Bright Blue
- Menu: Bright Cyan
- Results: Bright Green
- Errors: Bright Red

**Minimalist**
- All colors except errors in white

**Hacker Green**
- Classic green on black theme

Themes persist automatically in `~/.osintforge/settings.json`

## 📊 Module Details

### IP Intelligence Lookup
Performs comprehensive IP analysis including:
- Geolocation data
- ISP information
- VPN/Proxy detection
- Hosting provider identification
- Connection type analysis

### Domain Intelligence
Includes:
- DNS resolution
- WHOIS lookups
- Complete WHOIS record display
- IP resolution

### Username OSINT
Checks platforms:
- GitHub
- Twitter
- Instagram
- Reddit

### Port Scanner
Scans 19 common ports:
- HTTP/HTTPS (80, 443, 8080, 8443)
- SSH (22)
- FTP (21)
- SMTP (25, 465, 587)
- DNS (53)
- Database ports (MySQL, PostgreSQL, MongoDB)
- And more...

### Subdomain Enumeration
Tests 40+ common subdomain patterns:
- www, mail, ftp, api, dev, staging, admin, etc.

## 🔄 Workflow Examples

### Example 1: IP Investigation
```
1. Select "IP Intelligence Lookup" (1)
2. Enter: 8.8.8.8
3. View: Full IP details, GEO data, VPN status
4. Auto-saved to history
5. Option to export as JSON/CSV
```

### Example 2: Domain Recon
```
1. Select "Domain Intelligence" (2)
2. Enter: example.com
3. View: IP, WHOIS data, registrar info
4. Select "Subdomain Enumeration" (10)
5. View: Found subdomains
6. Export results for further analysis
```

### Example 3: User Profiling
```
1. Select "Username Search" (3)
2. Enter: john_doe
3. View: Results across GitHub, Twitter, Instagram, Reddit
4. Save to favorites for future reference
```

## 📈 Data Management

### Search History
- Automatically tracks all queries
- Shows timestamp and search count
- Displays recent 15 searches
- Access via option 14

### Favorites
- Save frequently analyzed targets
- Add custom labels
- Quick access from main menu
- Persistent storage

### Export Features
- **JSON Format** - Complete structured data
- **CSV Format** - Spreadsheet compatible
- Auto-timestamped filenames
- Organized in `~/.osintforge/exports/`

## 🔐 Security Considerations

- **Local Storage Only** - All data stored locally
- **No Cloud Upload** - Complete privacy
- **API Keys** - Password-protected entry
- **Settings Encryption-Ready** - Current plain-text, can be upgraded
- **Timeout Protection** - Configurable request timeouts

## 🛠️ Extending OSINTForge

### Adding a New Module

1. Create file in `modules/` directory:
   ```python
   # modules/my_module.py
   from core.banner import module_banner, output_banner, console
   from core.history import add_to_history
   from core.settings import get_theme
   
   def run_my_module():
       module_banner("My Module Title")
       # Your code here
       output_banner("Results")
       # Display results
       add_to_history("my_module", query_value)
   ```

2. Add import to `main.py`:
   ```python
   from modules.my_module import run_my_module
   ```

3. Add to menu in `core/menu.py`:
   ```python
   table.add_row("XX", "My Module Name", "[dim]Category[/dim]")
   ```

4. Add handler in `main.py`:
   ```python
   elif choice == "XX":
       run_my_module()
   ```

## 📝 Configuration Files

### settings.json
```json
{
  "theme": "default",
  "timeout": 10,
  "export_format": "json",
  "api_keys": {
    "virustotal": "",
    "shodan": "",
    "ipqualityscore": ""
  },
  "enable_history": true,
  "enable_favorites": true,
  "max_results": 100
}
```

## 🐛 Troubleshooting

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### API Timeout
- Increase timeout in Settings (Option 16, Choice 2)
- Check internet connection
- Verify target is accessible

### Rich Rendering Issues
```bash
# Update Rich library
pip install --upgrade rich
```

### Custom IP API Not Responding
- Check: https://suicixde.com/api/geoip/8.8.8.8
- Verify internet connectivity
- Try different IP address

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional OSINT modules
- Enhanced themes
- API integrations
- Performance optimizations
- Bug fixes
- Documentation improvements

### Contribution Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Rich Library** - Beautiful terminal rendering
- **Custom IP API** - Fast geolocation service (suicixde.com)
- **HackerTarget** - WHOIS lookup service
- **ip-api.com** - Enhanced geolocation data
- **Community Contributors** - Your support makes this better

## 📧 Contact & Support

- **Issues** - Report bugs via GitHub Issues
- **Suggestions** - Feature requests welcome
- **Questions** - Check existing issues first

## 🚀 Roadmap

- [ ] Database support for result caching
- [ ] Multi-threaded scanning
- [ ] Web interface (Flask/Django)
- [ ] API server mode
- [ ] Advanced filtering options
- [ ] Reporting in PDF format
- [ ] Integration with threat databases
- [ ] Real-time monitoring features

## ⚠️ Disclaimer

OSINTForge is designed for legitimate security research and authorized reconnaissance only. Users are responsible for:

- Obtaining proper authorization before testing
- Complying with applicable laws and regulations
- Respecting privacy and terms of service
- Responsible use of intelligence gathered

The developers are not responsible for misuse or unauthorized access.

---

**Made with ❤️ for the cybersecurity community**

*Latest Update: March 2026*
