from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from core.settings import get_theme

console = Console()

def display_main_menu():
    """Display the main menu with categorized modules."""
    theme = get_theme()
    
    # Create main menu table with categories
    table = Table(
        title=Text("🔍 OSINT MODULES", style=f"bold {theme['menu']}"),
        border_style=theme['banner'],
        show_header=True,
        header_style=f"bold {theme['results']}",
        padding=(0, 1),
        pad_edge=True
    )
    
    table.add_column("  #  ", style=f"bold {theme['field']}", width=5, justify="center")
    table.add_column("Module Name", style=f"{theme['results']}")
    table.add_column("Category", style=f"dim {theme['info']}", width=18)
    
    # Intelligence Gathering
    table.add_row("1", "IP Intelligence Lookup", "[dim]IP Analysis[/dim]")
    table.add_row("2", "Domain Intelligence", "[dim]Domain Analysis[/dim]")
    table.add_row("3", "Username OSINT Search", "[dim]User Profiling[/dim]")
    table.add_row("4", "Reverse DNS Lookup", "[dim]Network Mapping[/dim]")
    
    # Advanced Lookups
    table.add_row("5", "Email Address Lookup", "[dim]Account Analysis[/dim]")
    table.add_row("6", "DNS Records Lookup", "[dim]Domain Analysis[/dim]")
    table.add_row("7", "Phone Number Lookup", "[dim]Contact Verify[/dim]")
    table.add_row("8", "SSL Certificate Lookup", "[dim]Security Check[/dim]")
    
    # Network & Infrastructure
    table.add_row("9", "Website Information", "[dim]Web Analysis[/dim]")
    table.add_row("10", "Subdomain Enumeration", "[dim]Infrastructure[/dim]")
    table.add_row("11", "Port Scanner", "[dim]Service Discovery[/dim]")
    
    # Data Analysis
    table.add_row("12", "Hash Lookup & Analysis", "[dim]Data Verification[/dim]")
    table.add_row("13", "Geolocation Lookup", "[dim]Location Mapping[/dim]")
    
    # Utilities
    table.add_row("14", "Search History", "[dim]Data Management[/dim]")
    table.add_row("15", "Favorites", "[dim]Data Management[/dim]")
    
    # System
    table.add_row("16", "[yellow]⚙ Settings[/yellow]", "[dim yellow]Configuration[/dim yellow]")
    table.add_row("17", "[red]⏻ Exit[/red]", "[dim red]System[/dim red]")
    
    console.print(table)
    
    # Legend panel
    legend_text = f"""[{theme['field']}]💡 Tip:[/{theme['field']}] Use arrow keys or type numbers to select modules
[{theme['field']}]🎨 Current Theme:[/{theme['field']}] Access Settings (16) to change visual themes"""
    
    legend = Panel(
        legend_text,
        border_style=theme['info'],
        padding=(0, 1),
        expand=False
    )
    console.print(legend)


def get_menu_choice():
    """Get user's menu choice with Rich Prompt."""
    valid_choices = [str(i) for i in range(1, 18)]
    choice = Prompt.ask(
        "\n[bold cyan]Select option[/bold cyan]",
        choices=valid_choices,
        show_choices=False
    )
    return choice


def display_settings_menu():
    """Display the settings submenu with better styling."""
    theme = get_theme()
    
    table = Table(
        title=Text("⚙  SETTINGS", style=f"bold {theme['menu']}"),
        border_style=theme['banner'],
        show_header=True,
        header_style=f"bold {theme['results']}",
        padding=(0, 1),
        pad_edge=True
    )
    
    table.add_column("  #  ", style=f"bold {theme['field']}", width=5, justify="center")
    table.add_column("Setting", style=f"{theme['results']}")
    table.add_column("Description", style=f"dim {theme['info']}")
    
    table.add_row("1", "🎨 Change Theme", "Switch between color schemes")
    table.add_row("2", "⏱  Set Timeout", "Configure API timeout (seconds)")
    table.add_row("3", "💾 Export Format", "Choose JSON or CSV output")
    table.add_row("4", "🔑 API Keys", "Configure service credentials")
    table.add_row("5", "[dim]↩ Return[/dim]", "[dim]Back to main menu[/dim]")
    
    console.print(table)


def get_settings_choice():
    """Get user's settings choice."""
    valid_choices = ["1", "2", "3", "4", "5"]
    choice = Prompt.ask(
        "\n[bold cyan]Select option[/bold cyan]",
        choices=valid_choices,
        show_choices=False
    )
    return choice

