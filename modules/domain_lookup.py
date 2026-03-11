import socket
import requests
from rich.table import Table
from rich.panel import Panel
from core.banner import module_banner, output_banner, console


def run_domain_lookup():
    """Perform domain intelligence lookup with WHOIS data."""
    module_banner("Domain Intelligence Lookup")
    
    domain = input("Enter domain > ")
    
    try:
        ip = socket.gethostbyname(domain)
    except Exception as e:
        ip = f"[bold red]Could not resolve[/bold red] ({str(e)})"
    
    try:
        whois_api = f"https://api.hackertarget.com/whois/?q={domain}"
        whois_data = requests.get(whois_api, timeout=10).text
    except Exception as e:
        whois_data = f"[bold red]WHOIS lookup failed[/bold red]: {str(e)}"
    
    output_banner("Domain OSINT Result")
    
    # Create domain info table
    table = Table(
        title="[bold cyan]Domain Information[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green"
    )
    
    table.add_column("Field", style="bold yellow")
    table.add_column("Value", style="green")
    
    table.add_row("Domain", domain)
    table.add_row("Resolved IP", str(ip))
    
    console.print(table)
    
    # Display WHOIS data as a panel
    console.print("\n")
    whois_panel = Panel(
        whois_data,
        title="[bold cyan]WHOIS Data[/bold cyan]",
        border_style="cyan",
        expand=False
    )
    console.print(whois_panel)