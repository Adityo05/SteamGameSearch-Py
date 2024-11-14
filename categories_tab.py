import flet as ft
from game_grid import update_game_grid, game_grid

def create_categories_content(game_data, genres, page, navbar, tabs):
    genre_options = ["Select Genre"] + genres

    def on_genre_change(e):
        selected_genre = e.control.value
        filtered_games = filter_games_by_genre(selected_genre, game_data)
        update_game_grid(filtered_games, page, navbar, tabs)

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Dropdown(
                    options=[ft.dropdown.Option(text=genre) for genre in genre_options],
                    label="Select Genre",
                    on_change=on_genre_change
                ),
                game_grid
            ],
            scroll="auto",
            expand=True
        ),
        expand=True
    )

def filter_games_by_genre(genre, game_data):
    if genre == "Select Genre":
        return game_data
    return [game for game in game_data if genre in game["genres"]]
