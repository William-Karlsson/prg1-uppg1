import threading
import time
import requests

from core.visuals.color import colors

from server import start_server

def starta_server():
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    print("Server startad!")

def fråga_om_server():
    svar_starta_server = input("Hej! Vill du också öppna en lokal server(ja/nej)?")
    svar_starta_server = svar_starta_server.lower()


    if svar_starta_server in ['ja', 'nej']:
        if(svar_starta_server == 'ja'):
            starta_server()
    else:
        print("Inte tillåten input, skriv ja eller nej.")
        fråga_om_server()

    kör_spel()

def kör_spel():
    while True:
            response = requests.get("http://127.0.0.1:5000/data")
            data = response.json 
            print(data)
            time.sleep(1)