import json
import csv
from pathlib import Path
from datetime import datetime
from rich.console import Console

console = Console()

EXPORT_DIR = Path.home() / ".osintforge" / "exports"


def ensure_export_dir():
    """Create export directory if it doesn't exist."""
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)


def get_timestamp():
    """Get formatted timestamp for filenames."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def export_to_json(data, query_type, query_value):
    """Export data to JSON file."""
    ensure_export_dir()
    
    timestamp = get_timestamp()
    filename = f"{query_type}_{query_value}_{timestamp}.json"
    filepath = EXPORT_DIR / filename
    
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2, default=str)
        return True, str(filepath)
    except Exception as e:
        return False, str(e)


def export_to_csv(data, query_type, query_value):
    """Export data to CSV file."""
    ensure_export_dir()
    
    timestamp = get_timestamp()
    filename = f"{query_type}_{query_value}_{timestamp}.csv"
    filepath = EXPORT_DIR / filename
    
    try:
        if isinstance(data, list):
            if data and isinstance(data[0], dict):
                keys = data[0].keys()
                with open(filepath, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(data)
            else:
                with open(filepath, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(data)
        elif isinstance(data, dict):
            with open(filepath, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(data)
        else:
            return False, "Unsupported data format"
        
        return True, str(filepath)
    except Exception as e:
        return False, str(e)


def export_results(data, query_type, query_value, export_format="json"):
    """Export results in specified format."""
    if export_format.lower() == "json":
        return export_to_json(data, query_type, query_value)
    elif export_format.lower() == "csv":
        return export_to_csv(data, query_type, query_value)
    else:
        return False, "Unsupported format"


def display_export_success(filepath):
    """Display success message for export."""
    console.print(f"\n[bold green]✓ Results exported to:[/bold green]")
    console.print(f"[cyan]{filepath}[/cyan]\n")
