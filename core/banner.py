import os
from datetime import datetime
from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from core.settings import get_theme

# Global console instance for consistent styling
console = Console()

MAIN_BANNER = r"""
 ██████╗ ███████╗██╗███╗   ██╗████████╗██████╗  ██████╗ ███████╗███████╗
██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝██╔════╝
██║   ██║███████╗██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║███████╗█████╗  
██║   ██║╚════██║██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║╚════██║██╔══╝  
╚██████╔╝███████║██║██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████║███████╗
 ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝
"""

def clear():
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def show_main_banner():
    """Display the main banner with Rich Panel styling."""
    clear()
    theme = get_theme()
    banner_text = Text(MAIN_BANNER, style=f"bold {theme['banner']}")
    subtitle = Text("Multi-Purpose OSINT Intelligence Framework", style=f"italic {theme['info']}", justify="center")
    
    content = Group(
        banner_text,
        Align.center(subtitle)
    )
    
    panel = Panel(
        content,
        border_style=theme['banner'],
        expand=False,
        padding=(1, 2)
    )
    console.print(panel)


def module_banner(title):
    """Display module banner with title and UTC timestamp."""
    theme = get_theme()
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    title_text = Text(f"  ⚡ {title}  ", style=f"bold {theme['menu']} on {theme['results']}")
    timestamp_text = Text(f"⏱  {timestamp}", style=f"{theme['info']}")
    
    content = Group(
        Align.center(title_text),
        Align.center(timestamp_text)
    )
    
    panel = Panel(
        content,
        border_style=theme['menu'],
        padding=(1, 2),
        expand=False
    )
    console.print(panel)


def output_banner(title):
    """Display results separator banner."""
    theme = get_theme()
    banner_content = Text(f"  📊 {title}  ", style=f"bold {theme['results']}")
    panel = Panel(
        Align.center(banner_content),
        border_style=theme['results'],
        padding=(0, 2)
    )
    console.print(panel)