import json
import os
from pathlib import Path

SETTINGS_DIR = Path.home() / ".osintforge"
SETTINGS_FILE = SETTINGS_DIR / "settings.json"

# Theme definitions with color schemes
THEMES = {
    "default": {
        "name": "Default Cybersecurity",
        "banner": "magenta",
        "menu": "cyan",
        "results": "green",
        "error": "red",
        "info": "yellow",
        "field": "bold yellow",
        "success": "bold green"
    },
    "dark": {
        "name": "Dark Terminal",
        "banner": "bright_blue",
        "menu": "bright_cyan",
        "results": "bright_green",
        "error": "bright_red",
        "info": "bright_yellow",
        "field": "bright_magenta",
        "success": "bold bright_green"
    },
    "minimalist": {
        "name": "Minimalist",
        "banner": "white",
        "menu": "white",
        "results": "white",
        "error": "red",
        "info": "white",
        "field": "white",
        "success": "white"
    },
    "hacker": {
        "name": "Hacker Green",
        "banner": "bright_green",
        "menu": "bright_green",
        "results": "bright_green",
        "error": "bright_red",
        "info": "bright_yellow",
        "field": "bright_green",
        "success": "bold bright_green"
    }
}

DEFAULT_SETTINGS = {
    "theme": "default",
    "timeout": 10,
    "export_format": "json",
    "api_keys": {
        "virustotal": "",
        "shodan": "",
        "ipqualityscore": ""
    },
    "enable_history": True,
    "enable_favorites": True,
    "max_results": 100
}


def ensure_settings_dir():
    """Create settings directory if it doesn't exist."""
    SETTINGS_DIR.mkdir(parents=True, exist_ok=True)


def load_settings():
    """Load settings from file or create with defaults."""
    ensure_settings_dir()
    
    if SETTINGS_FILE.exists():
        try:
            with open(SETTINGS_FILE, 'r') as f:
                return json.load(f)
        except:
            return DEFAULT_SETTINGS.copy()
    else:
        save_settings(DEFAULT_SETTINGS.copy())
        return DEFAULT_SETTINGS.copy()


def save_settings(settings):
    """Save settings to file."""
    ensure_settings_dir()
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=2)


def get_theme():
    """Get current theme color scheme."""
    settings = load_settings()
    theme_name = settings.get("theme", "default")
    return THEMES.get(theme_name, THEMES["default"])


def set_theme(theme_name):
    """Set the active theme."""
    if theme_name not in THEMES:
        return False
    settings = load_settings()
    settings["theme"] = theme_name
    save_settings(settings)
    return True


def get_setting(key, default=None):
    """Get a specific setting value."""
    settings = load_settings()
    return settings.get(key, default)


def set_setting(key, value):
    """Set a specific setting value."""
    settings = load_settings()
    settings[key] = value
    save_settings(settings)


def get_api_key(service):
    """Get API key for a service."""
    settings = load_settings()
    return settings.get("api_keys", {}).get(service, "")


def set_api_key(service, key):
    """Set API key for a service."""
    settings = load_settings()
    if "api_keys" not in settings:
        settings["api_keys"] = {}
    settings["api_keys"][service] = key
    save_settings(settings)
