import dns.resolver
from rich.table import Table
from rich.panel import Panel
from core.banner import module_banner, output_banner, console
from core.history import add_to_history


def run_dns_lookup():
    """Perform comprehensive DNS record lookups."""
    module_banner("DNS Records Lookup")
    
    domain = input("Enter domain > ").strip()
    
    if not domain:
        console.print("[red]Error: Domain cannot be empty[/red]")
        return
    
    output_banner("DNS Records Results")
    
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']
    results = {}
    
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            results[record_type] = [str(rdata) for rdata in answers]
        except Exception as e:
            results[record_type] = [f"[dim]{str(e)[:50]}[/dim]"]
    
    # Display results
    for record_type in record_types:
        if results[record_type] and results[record_type][0]:
            content = "\n".join(results[record_type])
            panel = Panel(
                content,
                title=f"[bold cyan]{record_type} Records[/bold cyan]",
                border_style="cyan",
                expand=False
            )
            console.print(panel)
    
    add_to_history("dns", domain)
