# regler:
# Spelaren har en tärning (vanlig D6)
# Resultatet ska efter varje kast läggas på en totalsumma
# Efter varje kast får spelaren välja om hen vill kasta igen eller sluta kasta
# Målet är att komma så nära 21 som möjligt
# Om spelaren kommer över 21 så förlorar hen
# Får spelaren exakt 21 så vinner hen
# Stannar spelaren innan 21 får du bestämma vad som händer!

import random
from core.visuals.color import colors
from core.visuals.clear_screen import clear_screen
from core.save_data import load_data, save_data, add_money, increase_lost_games, increase_won_games

def intro():
    print(f'{colors.GREEN}Välkommen till 21!{colors.ENDC}\n')

    print("Målet är att komma så nära 21 som möjligt utan att gå över.")
    print("Du kastar en tärning (D6) och kan välja att kasta igen eller stanna.")
    print("Om du går över 21 förlorar du, om du får exakt 21 vinner du!\n")

    print("Om du får under eller över 21 tappar du samma antal MONEY™ som antal nummer ifrån 21 du slagit.")
    print("Om du får 21 får du 21 MONEY™!\n")

    print(f'{colors.CYAN}Lycka till!{colors.ENDC}\n')

def ask_play_again():
    choice = input("\nVill du spela igen? (ja/nej): ").lower()

    if choice in ['ja', 'nej']:
        if choice == 'ja':
            play_single_player()

        if choice == 'nej':
            from core.main_menu import display_main_menu

            display_main_menu()
    else:
        print(f"{colors.RED}Ogiltigt val. Vänligen skriv 'ja' eller 'nej'.{colors.ENDC}")
        ask_play_again()

def prompt():
    while True:
        choice = input("Vill du kasta tärningen? (ja/nej): ").strip().lower()
        if choice in ['ja', 'nej']:
            return choice
        else:
            print(f"{colors.RED}Ogiltigt val. Vänligen skriv 'ja' eller 'nej'.{colors.ENDC}")

def spel():
    total = 0

    while True:
        choice = prompt().lower()

        if choice == 'nej':
            print(f"{colors.PURPLE}Du valde att stanna med totalsumman: {total}.{colors.ENDC}")
            break

        kast = random.randint(1, 6)
        total += kast
        print(f"{colors.BLUE}Du kastade: {kast}. Totalsumma: {total}.{colors.ENDC}")

        if total > 21:
            print(f"{colors.RED}Du fick {total} och gick över 21! Du förlorade.{colors.ENDC}")

            add_money(-abs(total-21))

            print(f"{abs(total-21)} MONEY™ har raderats från ditt konto.")

            increase_lost_games()
            ask_play_again()
            break
        elif total == 21:
            print(f"{colors.GREEN}Grattis! Du fick exakt 21 och vann!{colors.ENDC}")

            add_money(21)

            print("21 MONEY™ har lagts till på ditt konto!")

            increase_won_games()
            ask_play_again()
            break

    if total < 21:
        add_money(-abs(total-21))

        print(f"{abs(total-21)} MONEY™ har raderats från ditt konto.")

        increase_lost_games()
        ask_play_again()

def play_single_player():
    clear_screen()
    intro()
    spel()