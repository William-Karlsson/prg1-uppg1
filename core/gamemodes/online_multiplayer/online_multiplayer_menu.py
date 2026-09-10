from core.visuals.color import colors
from core.main_menu import display_main_menu
from core.visuals.clear_screen import clear_screen
from core.gamemodes.online_multiplayer.online_multiplayer_handler import handle_start_and_join_server, join_specific_server, handle_start_server

menu_text = ["Joina server", "Starta och joina server", "Starta server", "Tillbaka till huvudmeny"]

def temp():
    # do nothing
    return

menu_functions = [join_specific_server, handle_start_and_join_server, lambda: handle_start_server(False), display_main_menu]

def display_online_menu():
    clear_screen()

    print(f"{colors.GREEN}Välkommen till online-läget!{colors.ENDC}")

    for i in range(0, len(menu_text)):
        print(f"{colors.PURPLE}[{colors.ENDC}{i + 1}{colors.PURPLE}]{colors.ENDC} {menu_text[i]}")

    prompt()

def prompt():
    chosen_option = input(f"Välj ett alternativ({colors.CYAN}1 - {len(menu_text)}{colors.ENDC}): ")

    try:
        chosen_option = int(chosen_option)

        if chosen_option > len(menu_functions) or chosen_option < 0: raise Exception

        menu_functions[chosen_option - 1]()
    except Exception as e:
        print(f"{colors.RED}Någonting gick fel! Vänligen skriv ett nummer på nytt.{colors.ENDC}")
        prompt()