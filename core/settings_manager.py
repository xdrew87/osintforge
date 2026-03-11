from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from core.settings import THEMES, get_setting, set_setting, set_theme, get_api_key, set_api_key

console = Console()


def settings_menu():
    """Main settings management menu."""
    from core.menu import display_settings_menu, get_settings_choice
    
    while True:
        console.print()  # Add spacing
        display_settings_menu()
        choice = get_settings_choice()
        
        if choice == "1":
            manage_themes()
        elif choice == "2":
            manage_timeout()
        elif choice == "3":
            manage_export_format()
        elif choice == "4":
            manage_api_keys()
        elif choice == "5":
            break
        
        input("\n[dim]Press ENTER to continue...[/dim]")


def manage_themes():
    """Theme selection interface."""
    console.clear()
    
    # Display current theme info
    current_theme = get_setting("theme", "default")
    current_desc = THEMES[current_theme].get("name", current_theme)
    
    header = Panel(
        Text(f"Current Theme: [bold cyan]{current_desc}[/bold cyan]", justify="center"),
        border_style="cyan",
        padding=(0, 1)
    )
    console.print(header)
    console.print()
    
    table = Table(
        title="[bold cyan]Available Themes[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green",
        padding=(0, 1),
        pad_edge=True
    )
    
    table.add_column("  #  ", style="bold yellow", width=5, justify="center")
    table.add_column("Theme Name", style="green")
    table.add_column("Description", style="cyan")
    
    theme_list = list(THEMES.items())
    for i, (key, theme) in enumerate(theme_list, 1):
        indicator = "✓ Current" if key == current_theme else "  "
        table.add_row(
            f"[yellow]{i}[/yellow]",
            f"[{theme.get('banner')}]{key.title()}[/{theme.get('banner')}]",
            theme.get("name", "")
        )
    
    console.print(table)
    console.print()
    
    choice = Prompt.ask(
        "[bold cyan]Select theme[/bold cyan]",
        choices=[str(i) for i in range(1, len(theme_list) + 1)],
        show_choices=False
    )
    
    selected_theme = theme_list[int(choice) - 1][0]
    set_theme(selected_theme)
    
    success = Panel(
        Text(f"✓ Theme changed to [bold cyan]{selected_theme.title()}[/bold cyan]", justify="center"),
        border_style="green",
        padding=(0, 1)
    )
    console.print(success)


def manage_timeout():
    """Timeout configuration."""
    console.clear()
    current = get_setting("timeout", 10)
    
    info_panel = Panel(
        f"[bold cyan]Current Timeout:[/bold cyan] [yellow]{current} seconds[/yellow]\n[dim]Valid range: 1 - 300 seconds[/dim]",
        border_style="cyan",
        padding=(0, 1)
    )
    console.print(info_panel)
    console.print()
    
    new_timeout = Prompt.ask(
        "Enter new timeout",
        default=str(current),
        show_default=True
    )
    
    try:
        timeout = int(new_timeout)
        if 1 <= timeout <= 300:
            set_setting("timeout", timeout)
            success = Panel(
                Text(f"✓ Timeout set to [bold green]{timeout} seconds[/bold green]", justify="center"),
                border_style="green",
                padding=(0, 1)
            )
            console.print(success)
        else:
            error = Panel(
                Text("[bold red]✗ Timeout must be between 1 and 300 seconds[/bold red]", justify="center"),
                border_style="red",
                padding=(0, 1)
            )
            console.print(error)
    except ValueError:
        error = Panel(
            Text("[bold red]✗ Invalid value - please enter a number[/bold red]", justify="center"),
            border_style="red",
            padding=(0, 1)
        )
        console.print(error)


def manage_export_format():
    """Export format selection."""
    console.clear()
    current = get_setting("export_format", "json")
    
    info_panel = Panel(
        f"[bold cyan]Current Format:[/bold cyan] [yellow]{current.upper()}[/yellow]",
        border_style="cyan",
        padding=(0, 1)
    )
    console.print(info_panel)
    console.print()
    
    formats = ["json", "csv"]
    
    table = Table(
        title="[bold cyan]Export Formats[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green",
        padding=(0, 1),
        pad_edge=True
    )
    
    table.add_column("  #  ", style="bold yellow", width=5, justify="center")
    table.add_column("Format", style="green")
    table.add_column("Description", style="cyan")
    
    table.add_row("1", "[green]JSON[/green]", "Universal data format, nested structure support")
    table.add_row("2", "[green]CSV[/green]", "Spreadsheet compatible, easy to import")
    
    console.print(table)
    console.print()
    
    choice = Prompt.ask(
        "[bold cyan]Select format[/bold cyan]",
        choices=["1", "2"],
        show_choices=False
    )
    
    selected_format = formats[int(choice) - 1]
    set_setting("export_format", selected_format)
    
    success = Panel(
        Text(f"✓ Export format set to [bold green]{selected_format.upper()}[/bold green]", justify="center"),
        border_style="green",
        padding=(0, 1)
    )
    console.print(success)


def manage_api_keys():
    """API keys configuration."""
    console.clear()
    
    header = Panel(
        Text("🔐 API Keys Configuration", justify="center"),
        border_style="yellow",
        padding=(0, 1)
    )
    console.print(header)
    console.print()
    
    services = ["virustotal", "shodan", "ipqualityscore"]
    
    table = Table(
        title="[bold cyan]Available Services[/bold cyan]",
        border_style="cyan",
        show_header=True,
        header_style="bold green",
        padding=(0, 1),
        pad_edge=True
    )
    
    table.add_column("  #  ", style="bold yellow", width=5, justify="center")
    table.add_column("Service", style="green")
    table.add_column("Status", style="cyan")
    
    for i, service in enumerate(services, 1):
        key = get_api_key(service)
        status = "[bold green]✓ Configured[/bold green]" if key else "[bold yellow]Not set[/bold yellow]"
        table.add_row(str(i), service.title(), status)
    
    console.print(table)
    console.print()
    
    choice = Prompt.ask(
        "[bold cyan]Select service to configure[/bold cyan]",
        choices=[str(i) for i in range(1, len(services) + 1)],
        default="1",
        show_choices=False
    )
    
    selected_service = services[int(choice) - 1]
    api_key = Prompt.ask(f"Enter {selected_service.upper()} API key", password=True)
    
    console.print()
    
    if api_key:
        set_api_key(selected_service, api_key)
        success = Panel(
            Text(f"✓ [bold green]{selected_service.title()} API key configured[/bold green]", justify="center"),
            border_style="green",
            padding=(0, 1)
        )
        console.print(success)
    else:
        warning = Panel(
            Text("[bold yellow]✗ API key not saved[/bold yellow]", justify="center"),
            border_style="yellow",
            padding=(0, 1)
        )
        console.print(warning)
