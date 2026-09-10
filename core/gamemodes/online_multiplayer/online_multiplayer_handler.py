import threading
import time
import requests

from core.visuals.color import colors

from core.gamemodes.online_multiplayer.online_server import start_server, set_no_server_logging

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

    print(f"Server startad på 127.0.0.1:{port}!", flush=True)

def handle_start_and_join_server():
    handle_start_server()
    join_specific_server()

def join_specific_server():
    ask_server_address()

def ask_server_address():
    address = input("Var god och skriv serveradressen du vill koppla till(eller 'exit' för att gå tillbaka): ")

    if address == 'exit':
        from core.gamemodes.online_multiplayer.online_multiplayer_menu import display_online_menu
        display_online_menu()
    else:
        try_connect_to_address(address, 5)

def try_connect_to_address(address, attempts):
    tried_attempts = 1
    
    while tried_attempts <= attempts:
        try:
            response = requests.get(address + '/data')

            if response.ok:
                print(response.text)
                break
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

def join_server():
    while True:
            response = requests.get("http://127.0.0.1:5000/data")
            data = response.json 
            print(data)
            time.sleep(1)