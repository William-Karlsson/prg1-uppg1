from core.save_data import load_data
from core.visuals.color import colors
from core.visuals.clear_screen import clear_screen

def view_player_profile():
    clear_screen()

    data = load_data()
    username = data["name"]
    slogan = data["slogan"]
    money = data["money"]
    won_games = data["won-games"]
    lost_games = data["lost-games"]
    total_games = int(won_games) + int(lost_games)

    print(f"{colors.GREEN}{username}{colors.ENDC}'s användarprofil:")

    print("\n")

    print(f"Slogan: {colors.PURPLE}{slogan}{colors.ENDC}")

    print("\n")

    print(f"Mängd MONEY™: {colors.PURPLE}{money}{colors.ENDC}")

    print("\n")

    print(f"Spel du vunnigt: {colors.PURPLE}{won_games}{colors.ENDC}")
    print(f"Spel du förlorat: {colors.PURPLE}{lost_games}{colors.ENDC}")
    print(f"Totalt antal spel: {colors.PURPLE}{total_games}{colors.ENDC}")

    print("\n")

    prompt()

def prompt():
    choice = input(f"{colors.CYAN}Skriv 'klar' för att gå tillbaka till huvudmenyn: {colors.CYAN}").lower()

    if choice == 'klar':
        from core.main_menu import display_main_menu
        display_main_menu()
    else:
        print(f"{colors.RED}Skriv 'klar' för att gå tillbaka.")
        prompt()
