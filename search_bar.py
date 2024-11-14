import flet as ft
from search import exponential_search 
from game_grid import update_game_grid  

def create_search_bar(game_data, page, navbar, tabs):
    def search_query_changed(e):
        query = e.control.value
        results = exponential_search(game_data, query, "name")
        update_game_grid(results, page, navbar, tabs)

    return ft.Container(
        content=ft.TextField(label="Search", on_change=search_query_changed),
        visible=False,
    )

