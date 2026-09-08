import time

from core.visuals.color import colors
from server import start_server
from core.player_card import load_data, save_data
from core.reused_info import start_money

from core.gamemodes.single_player import play_single_player

# Hantera om det är första gången spelaren öppnar appen

def handle_first_open():
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

    print(f"{colors.GREEN}Tack! Välkommen till Tärningsspelet, {name}!")

    time.sleep(5)

json = load_data()

if json == {}:
    handle_first_open()
    

# Meny-logik

menu_text = ["En spelare", "Två spelare(lokalt)", "Två spelare(mot bot)", "Online", "Stäng programmet"]

meny_functions = [play_single_player]

def menu():
    print(f"{colors.GREEN}Välkommen till tärningsspelet!{colors.ENDC} Vänligen välj ett alternativ för att köra igång!")

    for i in range(0, len(menu_text)):
        print(f"{colors.PURPLE}[{colors.ENDC}{i + 1}{colors.PURPLE}]{colors.ENDC} {menu_text[i]}")

    prompt()

def prompt():
    chosen_option = input(f"Välj ett alternativ({colors.CYAN}1 - {len(menu_text)}{colors.ENDC}): ")

    try:
        chosen_option = int(chosen_option)

        if chosen_option > len(meny_functions) or chosen_option < 0: raise Exception

        meny_functions[chosen_option - 1]()
    except:
        print(f"{colors.RED}Någonting gick fel! Vänligen skriv ett nummer på nytt.{colors.ENDC}")
        prompt()

menu()