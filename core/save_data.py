import json
import os

APP_NAME = "Williams Tärningspel"
FILE_NAME = "user_data.json"

def get_appdata_path():
    base_path = os.getenv('APPDATA') 

    # Liten fallback om APPDATA inte råkar existera som env var
    if not base_path:
        base_path = os.path.expanduser("~")
    
    app_folder = os.path.join(base_path, APP_NAME)
    
    # Se till att mappen faktiskt finns
    os.makedirs(app_folder, exist_ok=True)
    
    return os.path.join(app_folder, FILE_NAME)

def save_data(data): 
    filepath = get_appdata_path() 

    with open(filepath, 'w', encoding='utf-8') as f: 
        json.dump(data, f, indent=4)

def load_data():
    filepath = get_appdata_path()

    if not os.path.exists(filepath):
        # Ingen fil hittad, returnar tomt
        return {}
        
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def delete_save_file():
    filepath = get_appdata_path()

    if os.path.exists(filepath):
        os.remove(filepath)

def add_money(amount):
    try:
        playerData = load_data()
        playerData["money"] += amount
        save_data(playerData)
    except:
        print("Någonting gick fel med att uppdatera dina MONEY™, vänligen starta om programmet.")
        exit()

def increase_won_games():
    try:
        playerData = load_data()

        playerData["won-games"] += 1
        playerData["total-games"] += 1

        save_data(playerData)
    except:
        print("Någonting gick fel med att uppdatera spelstatistik, vänligen starta om programmet.")
        exit()
    
def increase_lost_games():
    try:
        playerData = load_data()

        playerData["lost-games"] += 1
        playerData["total-games"] += 1

        playerData
        save_data(playerData)
    except:
        print("Någonting gick fel med att uppdatera spelstatistik, vänligen starta om programmet.")
        exit()