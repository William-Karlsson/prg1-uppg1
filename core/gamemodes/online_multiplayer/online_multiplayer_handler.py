import threading
import time
import requests
import socket

from core.visuals.color import colors
from core.visuals.clear_screen import clear_screen

from core.gamemodes.online_multiplayer.online_server import start_server, set_no_server_logging
from core.gamemodes.online_multiplayer.online_multiplayer_game import start_multiplayer_game

def ask_port():
    port = input("Vänligen ange en port för servern: ")
    
    try:
        port = int(port)
    except:
        print(f"{colors.RED}Vänligen skriv ett (int) nummer.{colors.ENDC}")
        handle_start_server()
    
    return port

def handle_start_server(onSeperateThread = True):
    port = ask_port()

    if onSeperateThread:
        set_no_server_logging(True)
        server_thread = threading.Thread(target=start_server, args=(port,), daemon=True)
        server_thread.start()
    else:
        set_no_server_logging(False) # Slå på djupare loggning
        start_server(port)

    time.sleep(1)

    clear_screen()

    print(f"Server startad på {colors.PURPLE}http://0.0.0.0:{port}{colors.ENDC}", flush=True)
    print(f"Du bör kunna nå den genom {colors.PURPLE}http://{socket.gethostbyname(socket.gethostname())}:{port}{colors.ENDC} från andra enheter beroende på konfiguration.")

def handle_start_and_join_server():
    handle_start_server()
    join_specific_server()

def join_specific_server():
    address = ask_server_address()
    start_multiplayer_game(address)

def ask_server_address():
    address = input("Var god och skriv serveradressen du vill koppla till(eller 'exit' för att gå tillbaka): ")

    if address == 'exit':
        from core.gamemodes.online_multiplayer.online_multiplayer_menu import display_online_menu
        display_online_menu()
    else:
        return try_connect_to_address(address, 5)

def try_connect_to_address(address, attempts):

    tried_attempts = 1
    
    while tried_attempts <= attempts:
        try:
            response = requests.get(address + '/data')

            if response.ok:
                return address
            else:
                print("Request failed:", response.status_code)

                tried_attempts += 1

                if tried_attempts <= attempts:
                    print("Kunde inte koppla upp till server, provar igen")
                    time.sleep(3)
                else:
                    print(f"{colors.RED}Kunde inte koppla upp till server, vänligen prova en annan address eller se till att servern går att nå.{colors.ENDC}")
                    ask_server_address()
        except:
            tried_attempts += 1

            if tried_attempts <= attempts:
                print("Kunde inte koppla upp till server, provar igen")
                time.sleep(3)
            else:
                print(f"{colors.RED}Kunde inte koppla upp till server, vänligen prova en annan address eller se till att servern går att nå.{colors.ENDC}")
                ask_server_address()