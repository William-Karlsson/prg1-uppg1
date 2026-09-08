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
from core.clear_screen import clear_screen

def intro():
    print(f'{colors.GREEN}Välkommen till 21!{colors.ENDC}\n')

    print("Målet är att komma så nära 21 som möjligt utan att gå över.")
    print("Du kastar en tärning (D6) och kan välja att kasta igen eller stanna.")
    print("Om du går över 21 förlorar du, om du får exakt 21 vinner du!\n")

    print(f'{colors.CYAN}Lycka till!{colors.ENDC}\n')

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
        choice = prompt()
        if choice == 'nej':
            print(f"{colors.PURPLE}Du valde att stanna med totalsumman: {total}.{colors.ENDC}")
            break

        kast = random.randint(1, 6)
        total += kast
        print(f"{colors.BLUE}Du kastade: {kast}. Totalsumma: {total}.{colors.ENDC}")

        if total > 21:
            print(f"{colors.RED}Du gick över 21! Du förlorade.{colors.ENDC}")
            break
        elif total == 21:
            print(f"{colors.GREEN}Grattis! Du fick exakt 21 och vann!{colors.ENDC}")
            break

    if total < 21:
        # PUNISHMENTTTT
        print('Straff för att inte ta sig till 21 kommer senare, detta är här som placeholder för det.')
        input('Vill du spela igen? (ja/nej): ')

def play_single_player():
    clear_screen()
    intro()
    spel()