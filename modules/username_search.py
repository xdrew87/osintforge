import requests
from rich.table import Table
from core.banner import module_banner, output_banner, console

SITES = {
    "GitHub": "https://github.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://instagram.com/{}",
    "Reddit": "https://reddit.com/user/{}"
}


def run_username_search():
    """Search for username across multiple platforms."""
    module_banner("Username OSINT Search")
    
    username = input("Enter username > ")
    
    output_banner("Username Search Results")
    
    # Create results table
    table = Table(
        title="[bold cyan]Username Search Results[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green"
    )
    
    table.add_column("Platform", style="bold yellow")
    table.add_column("Status", style="bold")
    table.add_column("URL", style="cyan")
    
    for site, url in SITES.items():
        profile = url.format(username)
        
        try:
            r = requests.get(profile, timeout=5)
            
            if r.status_code == 200:
                table.add_row(
                    site,
                    "[bold green]✓ FOUND[/bold green]",
                    profile
                )
            else:
                table.add_row(
                    site,
                    "[bold yellow]✗ NOT FOUND[/bold yellow]",
                    profile
                )
        
        except Exception as e:
            table.add_row(
                site,
                "[bold red]✗ ERROR[/bold red]",
                f"[dim]{str(e)}[/dim]"
            )
    
    console.print(table)