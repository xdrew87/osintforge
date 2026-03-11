import requests
import hashlib
from rich.table import Table
from core.banner import module_banner, output_banner, console
from core.history import add_to_history


def identify_hash_type(hash_value):
    """Identify the type of hash."""
    hash_value = hash_value.strip().lower()
    length = len(hash_value)
    
    hash_types = {
        32: "MD5",
        40: "SHA1",
        64: "SHA256",
        128: "SHA512"
    }
    
    return hash_types.get(length, "Unknown")


def lookup_hash_virustotal(hash_value):
    """Lookup hash on VirusTotal (requires API key)."""
    # Demo mode - without actual API key
    return None, "VirusTotal lookup requires API key"


def lookup_hash_online(hash_value):
    """Lookup hash in online databases."""
    try:
        # Try common hash lookup services
        url = f"https://api.hashify.net/hash/identify?hash={hash_value}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return data, None
        else:
            return None, "Service temporarily unavailable"
    except Exception as e:
        return None, str(e)


def run_hash_lookup():
    """Perform hash lookup and analysis."""
    module_banner("Hash Lookup & Analysis")
    
    hash_value = input("Enter hash value > ").strip()
    
    if not hash_value:
        console.print("[red]Error: Hash cannot be empty[/red]")
        return
    
    output_banner("Hash Lookup Results")
    
    table = Table(
        title="[bold cyan]Hash Analysis[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green"
    )
    
    table.add_column("Field", style="bold yellow")
    table.add_column("Value", style="green")
    
    # Identify hash type
    hash_type = identify_hash_type(hash_value)
    table.add_row("Hash Type", hash_type)
    table.add_row("Hash Length", str(len(hash_value)))
    table.add_row("Hash Value", hash_value)
    
    # Attempt lookup
    result, error = lookup_hash_online(hash_value)
    
    if result:
        if isinstance(result, dict):
            for key, value in result.items():
                table.add_row(str(key).title(), str(value)[:50])
    elif error:
        table.add_row("Lookup Status", f"[yellow]{error}[/yellow]")
    
    # Security info
    if hash_type != "Unknown":
        if hash_type in ["MD5", "SHA1"]:
            console.print(table)
            console.print("\n[bold yellow]⚠ Warning:[/bold yellow] This hash algorithm is deprecated and should not be used for security purposes.\n")
        else:
            console.print(table)
            console.print("\n[bold green]✓[/bold green] This is a strong hash algorithm.\n")
    else:
        console.print(table)
    
    add_to_history("hash", hash_value[:16] + "...")
