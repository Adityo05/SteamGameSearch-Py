import flet as ft
from home_tab import create_home_content
from categories_tab import create_categories_content
from carousel import create_carousel
from game_grid import game_grid

def create_tabs(page, game_data, genres, navbar):
    global tabs

    def on_tab_change(e):
        if tabs.active_index == 0:  
            page.clean()
            page.add(navbar)
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
        elif tabs.active_index == 1:  
            page.clean()
            page.add(navbar)
            page.add(create_categories_content(game_data, genres, page, navbar, tabs))
            page.update()

    # Initialize tabs
    tabs = ft.Tabs(
        tabs=[
            ft.Tab(text="Home", content=ft.Container()),  
            ft.Tab(text="Categories", content=ft.Container())  
        ],
        on_change=on_tab_change
    )

    # Set the content of tabs after initialization
    tabs.tabs[0].content = create_home_content(game_data)
    tabs.tabs[1].content = create_categories_content(game_data, genres, page, navbar, tabs)

    return tabs
