import requests
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from core.banner import module_banner, output_banner, console
from core.settings import get_theme

API_URL = "https://suicixde.com/api/geoip/"


def run_ip_lookup():
    """Perform IP intelligence lookup and display results in a Rich Table."""
    module_banner("IP Intelligence Lookup")
    
    ip = input("Enter IP address > ").strip()
    
    if not ip:
        console.print("[red]❌ Error: IP address cannot be empty[/red]")
        return
    
    console.print("[cyan]🔍 Fetching IP intelligence data...[/cyan]")
    
    try:
        response = requests.get(API_URL + ip, timeout=10)
        data = response.json()
        
        output_banner("IP OSINT RESULT")
        
        theme = get_theme()
        
        # Create results table
        table = Table(
            title="[bold cyan]🌐 IP Intelligence Results[/bold cyan]",
            border_style="cyan",
            show_header=True,
            header_style=f"bold {theme['results']}",
            padding=(0, 1),
            pad_edge=True
        )
        
        table.add_column("Field", style=f"bold {theme['field']}", width=20)
        table.add_column("Value", style=f"{theme['results']}")
        
        table.add_row("IP Address", str(data.get('ip', 'N/A')))
        table.add_row("ISP", str(data.get('isp', 'N/A')))
        table.add_row("Organization", str(data.get('org', 'N/A')))
        table.add_row("Hostname", str(data.get('hostname', 'N/A')))
        table.add_row("Country", str(data.get('country_name', 'N/A')))
        table.add_row("Region", str(data.get('region', 'N/A')))
        table.add_row("City", str(data.get('city', 'N/A')))
        table.add_row("Latitude", str(data.get('latitude', 'N/A')))
        table.add_row("Longitude", str(data.get('longitude', 'N/A')))
        table.add_row("Connection Type", str(data.get('connection_type', 'N/A')))
        table.add_row(
            "VPN",
            "[bold red]⚠ Yes[/bold red]" if data.get('is_vpn') else "[bold green]✓ No[/bold green]"
        )
        table.add_row(
            "Proxy",
            "[bold red]⚠ Yes[/bold red]" if data.get('is_proxy') else "[bold green]✓ No[/bold green]"
        )
        table.add_row(
            "Hosting",
            "[bold red]⚠ Yes[/bold red]" if data.get('is_hosting') else "[bold green]✓ No[/bold green]"
        )
        
        console.print(table)
        
        # Summary panel
        console.print()
        vpn_status = "[bold red]⚠ VPN/Proxy Detected[/bold red]" if (data.get('is_vpn') or data.get('is_proxy')) else "[bold green]✓ Clean[/bold green]"
        summary = Panel(
            f"[bold cyan]IP:[/bold cyan] {data.get('ip')}\n[bold cyan]Location:[/bold cyan] {data.get('city')}, {data.get('country_name')}\n[bold cyan]Status:[/bold cyan] {vpn_status}",
            border_style="cyan",
            padding=(1, 1)
        )
        console.print(summary)
    
    except Exception as e:
        console.print(f"\n[bold red]❌ Error:[/bold red] {str(e)}\n")