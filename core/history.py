import json
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console()

HISTORY_DIR = Path.home() / ".osintforge"
HISTORY_FILE = HISTORY_DIR / "search_history.json"
FAVORITES_FILE = HISTORY_DIR / "favorites.json"


def ensure_history_dir():
    """Create history directory if it doesn't exist."""
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)


def _load_json_file(filepath):
    """Load JSON file safely."""
    ensure_history_dir()
    if filepath.exists():
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}


def _save_json_file(filepath, data):
    """Save data to JSON file."""
    ensure_history_dir()
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def add_to_history(query_type, query_value, results=None):
    """Add a search to history."""
    history = _load_json_file(HISTORY_FILE)
    
    key = f"{query_type}:{query_value}"
    history[key] = {
        "type": query_type,
        "value": query_value,
        "timestamp": datetime.now().isoformat(),
        "count": history.get(key, {}).get("count", 0) + 1
    }
    
    _save_json_file(HISTORY_FILE, history)


def get_history(limit=20):
    """Get recent searches."""
    history = _load_json_file(HISTORY_FILE)
    
    # Sort by timestamp (most recent first)
    sorted_history = sorted(
        history.values(),
        key=lambda x: x.get("timestamp", ""),
        reverse=True
    )
    
    return sorted_history[:limit]


def add_to_favorites(query_type, query_value, label=""):
    """Add item to favorites."""
    favorites = _load_json_file(FAVORITES_FILE)
    
    key = f"{query_type}:{query_value}"
    favorites[key] = {
        "type": query_type,
        "value": query_value,
        "label": label or query_value,
        "added": datetime.now().isoformat()
    }
    
    _save_json_file(FAVORITES_FILE, favorites)


def remove_from_favorites(query_type, query_value):
    """Remove item from favorites."""
    favorites = _load_json_file(FAVORITES_FILE)
    key = f"{query_type}:{query_value}"
    
    if key in favorites:
        del favorites[key]
        _save_json_file(FAVORITES_FILE, favorites)
        return True
    return False


def get_favorites():
    """Get all favorite items."""
    return _load_json_file(FAVORITES_FILE)


def display_history():
    """Display recent search history."""
    console.print()
    history = get_history()
    
    if not history:
        empty = Panel(
            Text("📭 No search history yet", justify="center"),
            border_style="yellow",
            padding=(1, 2)
        )
        console.print(empty)
        return
    
    table = Table(
        title="[bold cyan]📜 Recent Searches[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green",
        padding=(0, 1),
        pad_edge=True
    )
    
    table.add_column("Time", style="dim", width=19)
    table.add_column("Type", style="bold yellow", width=15)
    table.add_column("Query", style="green")
    table.add_column("Count", style="cyan", justify="center", width=8)
    
    for item in history[:15]:
        timestamp = datetime.fromisoformat(item["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
        query_type = item["type"].title()
        
        # Truncate long values
        query_value = item["value"]
        if len(query_value) > 40:
            query_value = query_value[:37] + "..."
        
        table.add_row(
            timestamp,
            query_type,
            query_value,
            str(item["count"])
        )
    
    console.print(table)
    console.print()


def display_favorites():
    """Display favorite items."""
    console.print()
    favorites = get_favorites()
    
    if not favorites:
        empty = Panel(
            Text("⭐ No favorites yet", justify="center"),
            border_style="yellow",
            padding=(1, 2)
        )
        console.print(empty)
        return
    
    table = Table(
        title="[bold cyan]⭐ Favorite Items[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green",
        padding=(0, 1),
        pad_edge=True
    )
    
    table.add_column("Type", style="bold yellow", width=15)
    table.add_column("Label", style="green")
    table.add_column("Value", style="cyan")
    
    for idx, item in enumerate(favorites.values(), 1):
        query_type = item["type"].title()
        
        # Truncate long values
        query_value = item["value"]
        if len(query_value) > 40:
            query_value = query_value[:37] + "..."
        
        table.add_row(
            query_type,
            item["label"][:25],
            query_value
        )
    
    console.print(table)
    console.print()
