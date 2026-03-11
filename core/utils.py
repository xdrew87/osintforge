from rich.prompt import Confirm
from rich.console import Console
from core.history import add_to_favorites, remove_from_favorites

console = Console()


def prompt_save_to_favorites(query_type, query_value):
    """Prompt user to save to favorites and handle it."""
    if Confirm.ask("[cyan]Save to favorites?[/cyan]", default=False):
        label = input("Enter a label for this favorite (optional) > ").strip()
        add_to_favorites(query_type, query_value, label or query_value)
        console.print("[bold green]✓ Saved to favorites[/bold green]")
