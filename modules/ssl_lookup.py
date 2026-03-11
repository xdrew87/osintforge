import ssl
import socket
from datetime import datetime
from rich.table import Table
from core.banner import module_banner, output_banner, console
from core.history import add_to_history


def get_ssl_certificate(domain):
    """Retrieve SSL certificate information."""
    try:
        context = ssl.create_default_context()
        conn = socket.create_connection((domain, 443), timeout=10)
        sock = context.wrap_socket(conn, server_hostname=domain)
        
        cert = sock.getpeercert()
        sock.close()
        
        return cert, None
    except Exception as e:
        return None, str(e)


def run_ssl_lookup():
    """Perform SSL certificate lookup and analysis."""
    module_banner("SSL Certificate Lookup")
    
    domain = input("Enter domain > ").strip()
    
    if not domain:
        console.print("[red]Error: Domain cannot be empty[/red]")
        return
    
    output_banner("SSL Certificate Results")
    
    cert, error = get_ssl_certificate(domain)
    
    table = Table(
        title="[bold cyan]SSL Certificate Information[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green"
    )
    
    table.add_column("Field", style="bold yellow")
    table.add_column("Value", style="green")
    
    if error:
        table.add_row("Status", f"[bold red]✗ Error[/bold red]")
        table.add_row("Error", error)
    else:
        try:
            table.add_row("Status", "[bold green]✓ SSL Present[/bold green]")
            
            # Subject
            subject = dict(x[0] for x in cert.get('subject', []))
            table.add_row("Common Name", subject.get('commonName', 'N/A'))
            table.add_row("Organization", subject.get('organizationName', 'N/A'))
            
            # Issuer
            issuer = dict(x[0] for x in cert.get('issuer', []))
            table.add_row("Issuer", issuer.get('commonName', 'N/A'))
            
            # Dates
            not_before = cert.get('notBefore', 'N/A')
            not_after = cert.get('notAfter', 'N/A')
            
            table.add_row("Valid From", not_before)
            table.add_row("Valid Until", not_after)
            
            # Check expiration
            if not_after != 'N/A':
                try:
                    expiry = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z")
                    days_left = (expiry - datetime.now()).days
                    
                    if days_left > 30:
                        status = f"[bold green]{days_left} days[/bold green]"
                    elif days_left > 0:
                        status = f"[bold yellow]{days_left} days[/bold yellow]"
                    else:
                        status = "[bold red]EXPIRED[/bold red]"
                    
                    table.add_row("Days Until Expiry", status)
                except:
                    pass
            
            # Alt names
            san = cert.get('subjectAltName', [])
            if san:
                alt_names = ", ".join([name[1] for name in san])
                table.add_row("Alt Names", alt_names)
            
            add_to_history("ssl", domain)
        
        except Exception as e:
            table.add_row("Error", str(e))
    
    console.print(table)
