import flet as ft

def create_navbar(page, search_bar_container):
    def toggle_search_bar(e):
        search_bar_container.visible = not search_bar_container.visible
        page.update()

    return ft.AppBar(
        color=ft.colors.WHITE,
        title=ft.Text("Steam"),
        bgcolor=ft.colors.BLACK26,
        actions=[
            ft.IconButton(icon=ft.icons.SEARCH, on_click=toggle_search_bar),
            search_bar_container,
        ],
    )