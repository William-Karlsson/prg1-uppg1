import time
import os

from core.visuals.color import colors

from core.save_data import load_data, save_data
from core.reused_info import start_money
from core.visuals.clear_screen import clear_screen

from core.main_menu import display_main_menu

# Hantera om det är första gången spelaren öppnar appen

def handle_first_open():
    clear_screen()

    print(f"{colors.GREEN}Välkommen till Tärningspelet, nykommare!{colors.ENDC}")

    print("Detta spel går ut på att slå tärningar! Väldigt glad att ha dig här idag.")

    print("För att diverse funktioner ska fungera korrekt krävs för lite information från dig!")
    print("\n")

    name = input(f"{colors.CYAN}Ange ditt användarnamn: {colors.ENDC}")
    slogan = input(f"{colors.CYAN}Ange din slogan(Vad som sägs till andra spelare när du vinner): {colors.ENDC}")

    player_information = {
        "name": name,
        "slogan": slogan,
        "money": start_money(),
        "won-games": 0,
        "lost-games": 0,
        "total-games": 0
    }

    save_data(player_information)

    print(f"{colors.GREEN}Tack, {name}!{colors.ENDC}")

    time.sleep(1)

    display_main_menu()

json = load_data()

if json == {}:
    handle_first_open()  
else:
    display_main_menu()