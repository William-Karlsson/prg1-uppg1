import requests
import time
import datetime
import msvcrt
import random

from core.visuals.clear_screen import clear_screen
from core.visuals.color import colors
from core.save_data import load_data, save_data, increase_lost_games, increase_won_games

def intro():

    clear_screen()

    print(f"{colors.GREEN}Välkommen till Online tärningsspelet!{colors.ENDC}\n")
    print("Detta spel handlar om att satsa och slå!\n")

    print("Du vinner om du kommer närmast 21.\n")
    print("I slutet av en runda ges hela potten till rundans vinnare. Vid fler än en spelare som är närmast 21 slumpas vinnaren mellan dem.\n")

    print(f"Skriv ett nummer för att addera den på potten(1-9)! {colors.RED}Du kan inte ta tillbaka det du har satsat!{colors.ENDC}")
    print("Du kan bara satsa innan rundan har börjat.\n")

    print("Vem som helst kan trycka på enter när som helst för att påbörja online-rundan! \n")

    print("Du kan även trycka på 'r' för att ladda om listan på spelare!")

def start_multiplayer_game(server_address):
    try:
        join_server(server_address)

        time.sleep(2)

        intro()

        player_info = load_data()

        show_current_players(server_address)

        response = requests.get(server_address + "/data")
        data = response.json()

        print(f"Din totala insats: {colors.GREEN}{data["players"][player_info["name"]]["bet"]}{colors.ENDC}")

        current_money = player_info["money"]
        print(f"Du har just nu {colors.PURPLE}{current_money} MONEY™{colors.ENDC} kvar i din användarprofil.")

        while True:
            player_info = load_data()
            current_money = player_info["money"]

            update_player_time(server_address)

            response = requests.get(server_address + "/data")
            data = response.json()

            if data["state"] == "lobby": 
                handle_lobby(server_address)
            if data["state"] == "in_game":
                handle_game(server_address)

            time.sleep(0.1)

    except Exception as e:
        print(e)
        time.sleep(5)

        from core.gamemodes.online_multiplayer.online_multiplayer_menu import display_online_menu
        display_online_menu()

def handle_lobby(server_address):
    player_info = load_data()
    current_money = player_info["money"]

    if msvcrt.kbhit():

        key = msvcrt.getch()

        while msvcrt.kbhit():
            key = msvcrt.getch()

        if key == b'\r':
            start_server_game(server_address)

        if key == b'r':
            response = requests.get(server_address + "/data")
            data = response.json()
            
            intro()

            show_current_players(server_address)

            print(f"Din totala insats: {colors.GREEN}{data["players"][player_info["name"]]["bet"]}{colors.ENDC}")

            player_info = load_data()
            current_money = player_info["money"]
            
            print(f"Du har just nu {colors.PURPLE}{current_money} MONEY™{colors.ENDC} kvar i din användarprofil.")

        if b'1' <= key <= b'9':
            number = int(key)

            if current_money >= number:

                place_bet(server_address, number)

                time.sleep(0.05)

                intro()

                show_current_players(server_address)

                response = requests.get(server_address + "/data")
                data = response.json()

                print(f"Din totala insats: {colors.GREEN}{data["players"][player_info["name"]]["bet"]}{colors.ENDC}")

                player_info = load_data()
                current_money = player_info["money"]

                print(f"Du har just nu {colors.PURPLE}{current_money} MONEY™{colors.ENDC} kvar i din användarprofil.")
            else:
                print(f"{colors.RED}Du har inte nog med MONEY™ kvar för det!{colors.ENDC}")

def game_intro():
    clear_screen()

    print(f"{colors.GREEN}Nu är det dags att spela!{colors.ENDC} Ditt mål är att slå och komma så nära 21 du kan! Lycka till.\n")

    print(f"{colors.PURPLE}Vill du slå din tärning?{colors.ENDC} Tryck 'j' för att slå tärningen eller 'n' för att stanna där du är!")
    print("Resultaten presenteras när alla är nöjda med sina totalsummor.")
    
def handle_game(server_address):
    total = 0

    hasSubmittedScore = False

    game_intro()

    while True:
        response = requests.get(server_address + "/data")
        data = response.json()

        if data["state"] == "in_game" and not hasSubmittedScore: 
            if msvcrt.kbhit():

                key = msvcrt.getch()

                while msvcrt.kbhit():
                    key = msvcrt.getch()

                if key == b'j':
                    kast = random.randint(1, 6)
                    total += kast
                    print(f"{colors.BLUE}Du kastade: {kast}. Totalsumma: {total}.{colors.ENDC}")

                if key == b'n':
                    print(f"{colors.CYAN}Du valde att stanna på {total}{colors.ENDC}, vänligen invänta de andra spelarna...")
                    submit_score(server_address, total)

                    hasSubmittedScore = True

        elif data["state"] == "finished":
            try:
                clear_screen()
                print("Alla spelare har nu slagit sin tärning!")
                time.sleep(1)
                print("Visar resultat om")
                print("3")
                time.sleep(2)
                print("2")
                time.sleep(2)
                print("1")
                time.sleep(2)

                clear_screen()

                winner = data["winner"]
                print(f"{colors.GREEN}{winner} vann denna runda med en totalsumma på {data["players"][winner]["score"]}{colors.ENDC}")
                print(f"Användaren har en liten hälsning till er förlorare: ")
                print(f"    {colors.CYAN}{data["players"][winner]["slogan"]}{colors.ENDC}")
                print(f"Den användaren får nu hela {colors.PURPLE}{data["total_pot"]} MONEY™!{colors.ENDC}")

                player_info = load_data()
                current_money = player_info["money"]
                username = player_info["name"]

                if(data["winner"] == username):
                    print(f"Grattis! Du vann hela {data["total_pot"]} MONEY™!")
                    player_info["money"] += data["total_pot"]
                    save_data(player_info)
                    
                    increase_won_games()
                else:
                    increase_lost_games()

                time.sleep(10)

                end_server_game(server_address)

                from core.gamemodes.online_multiplayer.online_multiplayer_menu import display_online_menu
                display_online_menu()
            except Exception as e:
                print(e)
                time.sleep(5)

                from core.gamemodes.online_multiplayer.online_multiplayer_menu import display_online_menu
                display_online_menu()

        update_player_time(server_address)

        time.sleep(0.1)

def end_server_game(server_address):
    try:
        address = f"{server_address}/stop_game"

        response = requests.post(
            address,
            json = {
            }
        )
    except Exception as e:
        print(e)
        time.sleep(5)

        from core.gamemodes.online_multiplayer.online_multiplayer_menu import display_online_menu
        display_online_menu()

def submit_score(server_address, score):
    try:
        player_info = load_data()

        username = player_info["name"]

        address = f"{server_address}/submit_score"

        response = requests.post(
            address,
            json = {
                "username": username,
                "score": score
            }
        )

        if not response.ok:
            print("Misslyckades:", response.json())
    except Exception as e:
        print(e)
        time.sleep(5)

        from core.gamemodes.online_multiplayer.online_multiplayer_menu import display_online_menu
        display_online_menu()

def show_current_players(server_address):
    print(f"{colors.PURPLE}Nuvarande spelare i server:{colors.ENDC}")
    response = requests.get(server_address + "/data")
    data = response.json()

    for username, player in data["players"].items():
        print("\t" + username)

def place_bet(server_address, amount):
    try:
        player_info = load_data()

        username = player_info["name"]

        address = f"{server_address}/add_bet"

        response = requests.post(
            address,
            json = {
                "username": username,
                "amount": amount
            }
        )

        if response.ok:
            player_info["money"] -= amount 
            save_data(player_info)
        else:
            print("Misslyckades:", response.json())
    except Exception as e:
        print(e)
        time.sleep(5)

        from core.gamemodes.online_multiplayer.online_multiplayer_menu import display_online_menu
        display_online_menu()


def start_server_game(server_address):
    try:
        address = f"{server_address}/start_game"

        response = requests.post(
            address,
            json = {
            }
        )

        if response.ok:
            print(f"Spelet har startat!")
        else:
            print("Misslyckades:", response.json())
    except Exception as e:
        print(e)
        time.sleep(5)

        from core.gamemodes.online_multiplayer.online_multiplayer_menu import display_online_menu
        display_online_menu()

def join_server(server_address):
    try:
        player_info = load_data()

        username = player_info["name"]
        slogan = player_info["slogan"]

        address = f"{server_address}/join"

        response = requests.post(
            address,
            json = {
                "username": username,
                "slogan": slogan
            }
        )

        if response.ok:
            print("Joinade servern!")
        else:
            print("Misslyckades:", response.json())
            time.sleep(5)

            from core.gamemodes.online_multiplayer.online_multiplayer_menu import display_online_menu
            display_online_menu()
    except Exception as e:
        print(e)
        time.sleep(5)

        from core.gamemodes.online_multiplayer.online_multiplayer_menu import display_online_menu
        display_online_menu()

def update_player_time(server_address):
    try:
        player_info = load_data()

        username = player_info["name"]

        address = f"{server_address}/update_time"
        time = int(datetime.datetime.utcnow().timestamp())

        response = requests.post(
            address,
            json = {
                "username": username,
                "time": time
            }
        )

        if not response.ok:
            print("Misslyckades:", response.json())
    except Exception as e:
        print(e)
        time.sleep(5)

        from core.gamemodes.online_multiplayer.online_multiplayer_menu import display_online_menu
        display_online_menu()
