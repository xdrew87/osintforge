import socket
from rich.table import Table
from core.banner import module_banner, output_banner, console


def run_reverse_dns():
    """Perform reverse DNS lookup and display results."""
    module_banner("Reverse DNS Lookup")
    
    ip = input("Enter IP address > ")
    
    try:
        host, aliases, addresses = socket.gethostbyaddr(ip)
        
        output_banner("Reverse DNS Result")
        
        # Create results table
        table = Table(
            title="[bold cyan]Reverse DNS Results[/bold cyan]",
            border_style="cyan",
            show_header=True,
            header_style="bold green"
        )
        
        table.add_column("Field", style="bold yellow")
        table.add_column("Value", style="green")
        
        table.add_row("Hostname", host)
        table.add_row("Aliases", ", ".join(aliases) if aliases else "[dim]None[/dim]")
        table.add_row("Addresses", ", ".join(addresses) if addresses else "[dim]None[/dim]")
        
        console.print(table)
    
    except Exception as e:
        console.print(f"[bold red]❌ Lookup failed:[/bold red] {str(e)}")