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
    
    print(f"Data sparad till: {filepath}")

def load_data():
    filepath = get_appdata_path()

    if not os.path.exists(filepath):
        print("Ingen fil hittad, returnar tom data.")
        return {}
        
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def delete_save_file():
    filepath = get_appdata_path()

    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Fil borttagen: {filepath}")