from rich.console import Console
from core.banner import show_main_banner, console
from core.menu import display_main_menu, get_menu_choice
from core.settings_manager import settings_menu
from core.history import display_history, display_favorites

# Original modules
from modules.ip_lookup import run_ip_lookup
from modules.domain_lookup import run_domain_lookup
from modules.username_search import run_username_search
from modules.reverse_dns import run_reverse_dns

# New modules
from modules.email_lookup import run_email_lookup
from modules.dns_lookup import run_dns_lookup
from modules.phone_lookup import run_phone_lookup
from modules.ssl_lookup import run_ssl_lookup
from modules.website_info import run_website_info
from modules.subdomain_enum import run_subdomain_enum
from modules.port_scanner import run_port_scanner
from modules.hash_lookup import run_hash_lookup
from modules.geolocation import run_geolocation


def menu():
    """Main menu loop for OSINT Forge."""
    while True:
        show_main_banner()
        display_main_menu()
        
        choice = get_menu_choice()
        
        if choice == "1":
            run_ip_lookup()
        elif choice == "2":
            run_domain_lookup()
        elif choice == "3":
            run_username_search()
        elif choice == "4":
            run_reverse_dns()
        elif choice == "5":
            run_email_lookup()
        elif choice == "6":
            run_dns_lookup()
        elif choice == "7":
            run_phone_lookup()
        elif choice == "8":
            run_ssl_lookup()
        elif choice == "9":
            run_website_info()
        elif choice == "10":
            run_subdomain_enum()
        elif choice == "11":
            run_port_scanner()
        elif choice == "12":
            run_hash_lookup()
        elif choice == "13":
            run_geolocation()
        elif choice == "14":
            console.clear()
            display_history()
        elif choice == "15":
            console.clear()
            display_favorites()
        elif choice == "16":
            console.clear()
            settings_menu()
        elif choice == "17":
            console.print("\n[bold green]Exiting OSINT Console. Goodbye![/bold green]\n")
            break
        
        input("\n[dim]Press ENTER to return to main menu...[/dim]")


if __name__ == "__main__":
    menu()