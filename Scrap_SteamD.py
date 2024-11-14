import os
import requests
import json
import time
from bs4 import BeautifulSoup
import re

STEAMSPY_API_URL = "https://steamspy.com/api.php"
STEAM_STORE_API_URL = "https://store.steampowered.com/api/appdetails"

def get_game_list_from_steamspy():
    params = {'request': 'all'}
    try:
        response = requests.get(STEAMSPY_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching game list from SteamSpy: {e}")
        return None

def get_game_details_from_steamspy(appid):
    params = {'request': 'appdetails', 'appid': appid}
    try:
        response = requests.get(STEAMSPY_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching details for appid {appid} from SteamSpy: {e}")
        return None

def get_game_info_from_steam_store(appid, language='english'):
    params = {'appids': appid, 'l': language}
    try:
        response = requests.get(STEAM_STORE_API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if str(appid) in data and 'data' in data[str(appid)]:
            game_data = data[str(appid)]['data']
            description_html = game_data.get('detailed_description', 'No description available')
            soup = BeautifulSoup(description_html, "html.parser")
            description = soup.get_text(separator='\n').strip()
            images = {
                'header_image': game_data.get('header_image', ''),
                'screenshots': [s['path_thumbnail'] for s in game_data.get('screenshots', [])]
            }
            return description, images
        else:
            print(f"No 'data' field in response for appid {appid}")
            print(data)
            return 'No description available', {}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching description for appid {appid} from Steam Store: {e}")
        return 'No description available', {}

def download_image(url, game_name, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Clean game_name to remove invalid characters for directory names in Windows
        game_name_clean = re.sub(r'[\\/:"*?<>|]', '', game_name)
        folder = os.path.join('game_images', game_name_clean)
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return file_path
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image from {url}: {e}")
        return None

def gather_game_data(limit=50, num_screenshots=5):
    game_list = get_game_list_from_steamspy()
    if game_list:
        detailed_games = []
        count = 0
        
        for appid, game in game_list.items():
            if count >= limit:
                break
            details = get_game_details_from_steamspy(appid)
            if details:
                description, images = get_game_info_from_steam_store(appid, language='english')
                
                header_image_path = None
                if images.get('header_image'):
                    header_image_path = download_image(images['header_image'], game['name'], f"{appid}_header.jpg")

                screenshot_paths = []
                for i, screenshot_url in enumerate(images.get('screenshots', [])):
                    if i >= num_screenshots:
                        break
                    screenshot_path = download_image(screenshot_url, game['name'], f"{appid}_screenshot_{i}.jpg")
                    if screenshot_path:
                        screenshot_paths.append(screenshot_path)
                
                game_info = {
                    'appid': appid,
                    'name': game['name'].strip(),
                    'genres': details.get('genre', 'Unknown'),
                    'price': details.get('price', 'Unknown'),
                    'description': description,
                    'header_image': header_image_path,
                    'screenshots': screenshot_paths
                }
                detailed_games.append(game_info)
            else:
                print(f"No details found for appid {appid}")
            time.sleep(1)  # Avoid too many requests in a short time
            count += 1

        # Save data to a JSON file
        with open("detailed_game_list.json", "w") as file:
            json.dump(detailed_games, file, indent=4)

        print("Detail game telah didapat dan disimpan di detailed_game_list.json")
    else:
        print("Gagal mengambil detail game")

gather_game_data()