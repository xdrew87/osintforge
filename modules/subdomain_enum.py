import requests
from rich.table import Table
from rich.progress import Progress
from core.banner import module_banner, output_banner, console
from core.history import add_to_history

# Common subdomains to enumerate
COMMON_SUBDOMAINS = [
    "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1",
    "webdisk", "ns2", "cpanel", "whm", "autodiscover", "autoconfig",
    "m", "mobile", "api", "dev", "staging", "test", "admin", "cms",
    "blog", "shop", "forum", "wiki", "support", "docs", "cdn", "images",
    "static", "download", "news", "events", "calendar", "files",
    "server", "vpn", "client", "gateway", "backup"
]


def check_subdomain(subdomain, domain):
    """Check if subdomain exists."""
    try:
        url = f"https://{subdomain}.{domain}"
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code < 400
    except:
        # Try HTTP
        try:
            url = f"http://{subdomain}.{domain}"
            response = requests.head(url, timeout=5, allow_redirects=True)
            return response.status_code < 400
        except:
            return False


def run_subdomain_enum():
    """Enumerate subdomains for a domain."""
    module_banner("Subdomain Enumeration")
    
    domain = input("Enter domain > ").strip()
    
    if not domain:
        console.print("[red]Error: Domain cannot be empty[/red]")
        return
    
    output_banner("Subdomain Enumeration Results")
    
    found_subdomains = []
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Enumerating subdomains...", total=len(COMMON_SUBDOMAINS))
        
        for subdomain in COMMON_SUBDOMAINS:
            if check_subdomain(subdomain, domain):
                found_subdomains.append(subdomain)
            progress.update(task, advance=1)
    
    # Display results
    if found_subdomains:
        table = Table(
            title="[bold cyan]Found Subdomains[/bold cyan]",
            border_style="cyan",
            show_header=True,
            header_style="bold green"
        )
        
        table.add_column("Subdomain", style="green")
        table.add_column("Full URL", style="cyan")
        
        for subdomain in found_subdomains:
            full_url = f"{subdomain}.{domain}"
            table.add_row(subdomain, full_url)
        
        console.print(table)
        
        console.print(f"\n[bold green]✓ Found {len(found_subdomains)} subdomains[/bold green]")
    else:
        console.print("[yellow]No common subdomains found[/yellow]")
    
    add_to_history("subdomain", domain)
