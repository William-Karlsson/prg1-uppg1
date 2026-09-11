from core.visuals.color import colors
from core.save_data import load_data, delete_save_file
from core.visuals.clear_screen import clear_screen

from core.gamemodes.single_player import play_single_player
from core.gamemodes.online_multiplayer.online_multiplayer_core import play_online_multiplayer
from core.player_profile_viewer import view_player_profile

menu_text = ["En spelare", "Online", "Stäng programmet", "Radera spelardata från hårddisk", "Visa spelarprofil"]

def delete_save():
    from main import handle_first_open
    delete_save_file()
    handle_first_open()

menu_functions = [play_single_player, play_online_multiplayer, quit, delete_save, view_player_profile]

def display_main_menu():
    clear_screen()

    print(f"{colors.GREEN}Välkommen till tärningsspelet!{colors.ENDC} Vänligen välj ett alternativ för att köra igång!")

    for i in range(0, len(menu_text)):
        print(f"{colors.PURPLE}[{colors.ENDC}{i + 1}{colors.PURPLE}]{colors.ENDC} {menu_text[i]}")

    prompt()

def prompt():
    chosen_option = input(f"Välj ett alternativ({colors.CYAN}1 - {len(menu_text)}{colors.ENDC}): ")

    try:
        chosen_option = int(chosen_option)

        if chosen_option > len(menu_functions) or chosen_option < 0: raise Exception("Oh noo")

        menu_functions[chosen_option - 1]()
    except Exception as e:
        print(f"{colors.RED}Någonting gick fel! Vänligen skriv ett nummer på nytt.{colors.ENDC}")
        prompt()