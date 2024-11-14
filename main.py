import flet as ft 
from navbar import create_navbar
from search_bar import create_search_bar
from tabs import create_tabs
from game_data import load_game_data
from game_grid import update_game_grid

game_data, genres = load_game_data("detailed_game_list.json")

def main(page: ft.Page):
    page.title = "Steam"
    page.bgcolor = ft.colors.BLUE_GREY_900
  
    search_bar_container = None
    navbar = None
    tabs = None
       
    search_bar_container = create_search_bar(game_data, page, navbar, tabs) 
    navbar = create_navbar(page, search_bar_container)
    tabs = create_tabs(page, game_data, genres, navbar)

    search_bar_container = create_search_bar(game_data, page, navbar, tabs)

    update_game_grid(game_data, page, navbar, tabs)


    page.appbar = navbar
    page.add(
        ft.Container(
            content=ft.Stack(
                controls=[tabs],
                # scroll="auto",
                expand=True
            ),
            expand=True
        )
    )
    page.update()

# Menjalankan aplikasi
ft.app(target=main)
