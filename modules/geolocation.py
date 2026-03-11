import requests
from rich.table import Table
from rich.panel import Panel
from core.banner import module_banner, output_banner, console
from core.history import add_to_history


def get_geolocation(ip):
    """Get geolocation data for IP address."""
    try:
        # Using ip-api.com free service
        url = f"http://ip-api.com/json/{ip}?fields=status,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,isp,org,as,mobile,proxy,hosting,query"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 'success':
                return data, None
            else:
                return None, data.get('message', 'Unknown error')
        else:
            return None, f"HTTP {response.status_code}"
    except Exception as e:
        return None, str(e)


def run_geolocation():
    """Perform geolocation lookup for IP addresses."""
    module_banner("Geolocation Lookup")
    
    ip = input("Enter IP address > ").strip()
    
    if not ip:
        console.print("[red]Error: IP cannot be empty[/red]")
        return
    
    output_banner("Geolocation Results")
    
    data, error = get_geolocation(ip)
    
    if error:
        console.print(f"[bold red]Error: {error}[/bold red]")
        return
    
    # Main info table
    table = Table(
        title="[bold cyan]Geolocation Information[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green"
    )
    
    table.add_column("Field", style="bold yellow")
    table.add_column("Value", style="green")
    
    table.add_row("IP Address", data.get('query', 'N/A'))
    table.add_row("Country", f"{data.get('country', 'N/A')} ({data.get('countryCode', 'N/A')})")
    table.add_row("Region", data.get('regionName', 'N/A'))
    table.add_row("City", data.get('city', 'N/A'))
    table.add_row("Postal Code", data.get('zip', 'N/A'))
    table.add_row("Timezone", data.get('timezone', 'N/A'))
    
    console.print(table)
    
    # Coordinates panel
    console.print("\n")
    lat = data.get('lat', 'N/A')
    lon = data.get('lon', 'N/A')
    coords_content = f"[bold yellow]Latitude:[/bold yellow] {lat}\n[bold yellow]Longitude:[/bold yellow] {lon}"
    
    if lat != 'N/A' and lon != 'N/A':
        coords_content += f"\n[dim]Maps URL: https://maps.google.com/?q={lat},{lon}[/dim]"
    
    coords_panel = Panel(
        coords_content,
        title="[bold cyan]Coordinates[/bold cyan]",
        border_style="cyan"
    )
    console.print(coords_panel)
    
    # Network info table
    console.print("\n")
    net_table = Table(
        title="[bold cyan]Network Information[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green"
    )
    
    net_table.add_column("Field", style="bold yellow")
    net_table.add_column("Value", style="green")
    
    net_table.add_row("ISP", data.get('isp', 'N/A'))
    net_table.add_row("Organization", data.get('org', 'N/A'))
    net_table.add_row("AS", data.get('as', 'N/A'))
    net_table.add_row(
        "Mobile",
        "[bold green]Yes[/bold green]" if data.get('mobile') else "[bold red]No[/bold red]"
    )
    net_table.add_row(
        "Proxy",
        "[bold red]Yes[/bold red]" if data.get('proxy') else "[bold green]No[/bold green]"
    )
    net_table.add_row(
        "Hosting",
        "[bold red]Yes[/bold red]" if data.get('hosting') else "[bold green]No[/bold green]"
    )
    
    console.print(net_table)
    
    add_to_history("geolocation", ip)
