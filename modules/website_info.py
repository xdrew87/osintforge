import requests
from rich.table import Table
from rich.panel import Panel
from core.banner import module_banner, output_banner, console
from core.history import add_to_history


def get_website_info(domain):
    """Fetch website headers and metadata."""
    try:
        # Add http if no scheme
        url = domain if domain.startswith(('http://', 'https://')) else f"https://{domain}"
        
        response = requests.head(url, allow_redirects=True, timeout=10)
        headers = response.headers
        
        return {
            'status_code': response.status_code,
            'headers': dict(headers),
            'url': response.url,
            'history': response.history
        }, None
    except Exception as e:
        return None, str(e)


def run_website_info():
    """Lookup website information and headers."""
    module_banner("Website Information Lookup")
    
    domain = input("Enter domain or URL > ").strip()
    
    if not domain:
        console.print("[red]Error: Domain cannot be empty[/red]")
        return
    
    output_banner("Website Information Results")
    
    info, error = get_website_info(domain)
    
    if error:
        console.print(f"[bold red]Error: {error}[/bold red]")
        return
    
    # Basic info table
    table = Table(
        title="[bold cyan]Website Information[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green"
    )
    
    table.add_column("Field", style="bold yellow")
    table.add_column("Value", style="green")
    
    status_color = "green" if 200 <= info['status_code'] < 400 else "red"
    table.add_row("Status Code", f"[{status_color}]{info['status_code']}[/{status_color}]")
    table.add_row("Final URL", info['url'])
    
    if info['history']:
        redirects = " → ".join([f"{r.status_code}" for r in info['history']])
        table.add_row("Redirects", f"[yellow]{redirects}[/yellow]")
    
    console.print(table)
    
    # Headers panel
    console.print("\n")
    important_headers = [
        'Server', 'X-Powered-By', 'X-AspNet-Version', 'X-Frame-Options',
        'X-Content-Type-Options', 'Strict-Transport-Security', 'Content-Type'
    ]
    
    header_content = ""
    for header in important_headers:
        value = info['headers'].get(header, info['headers'].get(header.lower(), 'N/A'))
        if value != 'N/A':
            header_content += f"[bold yellow]{header}:[/bold yellow] {value}\n"
    
    if header_content:
        panel = Panel(
            header_content.strip(),
            title="[bold cyan]Important Headers[/bold cyan]",
            border_style="cyan"
        )
        console.print(panel)
    
    add_to_history("website", domain)
