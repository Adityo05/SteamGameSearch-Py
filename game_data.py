import json

def load_game_data(json_file):
    with open(json_file, "r") as file:
        games = json.load(file)
        all_genres = set()
        for game in games:
            game_genres = game["genres"].split(", ")
            game["genres"] = game_genres
            all_genres.update(game_genres)
        return games, sorted(all_genres)
