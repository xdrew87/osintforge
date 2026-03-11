import re
from email_validator import validate_email, EmailNotValidError
from rich.table import Table
from core.banner import module_banner, output_banner, console
from core.history import add_to_history


def run_email_lookup():
    """Validate and check email addresses."""
    module_banner("Email Address Lookup")
    
    email = input("Enter email address > ").strip()
    
    if not email:
        console.print("[red]Error: Email cannot be empty[/red]")
        return
    
    output_banner("Email Validation Results")
    
    table = Table(
        title="[bold cyan]Email Analysis[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green"
    )
    
    table.add_column("Field", style="bold yellow")
    table.add_column("Value", style="green")
    
    try:
        # Validate email format
        valid = validate_email(email)
        email_normalized = valid.email
        
        table.add_row("Status", "[bold green]✓ Valid[/bold green]")
        table.add_row("Email", email_normalized)
        
        # Extract parts
        local, domain = email_normalized.split('@')
        table.add_row("Local Part", local)
        table.add_row("Domain", domain)
        
        # Check for common providers
        common_providers = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"]
        provider_type = "Personal Provider" if domain in common_providers else "Custom Domain"
        table.add_row("Provider Type", provider_type)
        
        # Check for disposable email (basic check)
        disposable_domains = ["tempmail.com", "guerrillamail.com", "10minutemail.com"]
        is_disposable = "Yes" if domain in disposable_domains else "No"
        table.add_row("Disposable Email", is_disposable)
        
        add_to_history("email", email)
        
    except EmailNotValidError as e:
        table.add_row("Status", "[bold red]✗ Invalid[/bold red]")
        table.add_row("Error", str(e))
    
    console.print(table)
