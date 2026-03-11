import re
from rich.table import Table
from core.banner import module_banner, output_banner, console
from core.history import add_to_history


def validate_phone(phone):
    """Validate phone number format."""
    # Remove common separators
    cleaned = re.sub(r'[\s\-\(\)]', '', phone)
    
    # Check if it's numeric
    if not cleaned.isdigit():
        return None, "Invalid characters"
    
    # Check length (typically 10-15 digits for international)
    if len(cleaned) < 10 or len(cleaned) > 15:
        return None, "Invalid length"
    
    return cleaned, None


def get_country_code(phone):
    """Guess country from phone number format."""
    country_codes = {
        "+1": "USA/Canada",
        "+44": "UK",
        "+33": "France",
        "+49": "Germany",
        "+86": "China",
        "+81": "Japan",
        "+91": "India",
        "+55": "Brazil",
        "+27": "South Africa",
        "+61": "Australia"
    }
    
    for code, country in country_codes.items():
        if phone.startswith(code):
            return country
    
    return "Unknown"


def run_phone_lookup():
    """Perform phone number analysis and validation."""
    module_banner("Phone Number Lookup")
    
    phone = input("Enter phone number (with country code +X) > ").strip()
    
    if not phone:
        console.print("[red]Error: Phone number cannot be empty[/red]")
        return
    
    output_banner("Phone Number Analysis Results")
    
    table = Table(
        title="[bold cyan]Phone Number Analysis[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green"
    )
    
    table.add_column("Field", style="bold yellow")
    table.add_column("Value", style="green")
    
    # Validate
    cleaned, error = validate_phone(phone)
    
    if error:
        table.add_row("Status", f"[bold red]✗ {error}[/bold red]")
    else:
        table.add_row("Status", "[bold green]✓ Valid[/bold green]")
        table.add_row("Original", phone)
        table.add_row("Cleaned", cleaned)
        table.add_row("Length", str(len(cleaned)))
        
        # Detect country
        country = get_country_code(phone)
        table.add_row("Country", country)
        
        # Format variations
        if cleaned.startswith("1"):
            # US/Canada format
            formatted = f"+1-{cleaned[1:4]}-{cleaned[4:7]}-{cleaned[7:]}"
            table.add_row("US Format", formatted)
        
        add_to_history("phone", phone)
    
    console.print(table)
