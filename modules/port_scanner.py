import socket
from rich.table import Table
from rich.progress import Progress
from core.banner import module_banner, output_banner, console
from core.history import add_to_history

# Common ports to scan
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    465: "SMTPS",
    587: "SMTP TLS",
    993: "IMAPS",
    995: "POP3S",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP Alt",
    8443: "HTTPS Alt",
    27017: "MongoDB"
}


def check_port(host, port, timeout=2):
    """Check if port is open."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False


def run_port_scanner():
    """Scan common ports on a host."""
    module_banner("Port Scanner")
    
    host = input("Enter hostname or IP > ").strip()
    
    if not host:
        console.print("[red]Error: Host cannot be empty[/red]")
        return
    
    output_banner("Port Scan Results")
    
    open_ports = []
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Scanning ports...", total=len(COMMON_PORTS))
        
        for port, service in COMMON_PORTS.items():
            if check_port(host, port):
                open_ports.append((port, service))
            progress.update(task, advance=1)
    
    # Display results
    if open_ports:
        table = Table(
            title="[bold cyan]Open Ports[/bold cyan]",
            border_style="cyan",
            show_header=True,
            header_style="bold green"
        )
        
        table.add_column("Port", style="bold yellow")
        table.add_column("Service", style="green")
        table.add_column("Status", style="bold green")
        
        for port, service in sorted(open_ports):
            table.add_row(str(port), service, "✓ OPEN")
        
        console.print(table)
        console.print(f"\n[bold green]✓ Found {len(open_ports)} open ports[/bold green]\n")
    else:
        console.print("[yellow]No open ports found on common ports[/yellow]\n")
    
    add_to_history("port_scan", host)
