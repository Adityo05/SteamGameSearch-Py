import flet as ft
from game_details import show_game_details

USD_TO_IDR = 16000

def convert_price(price_usd):
    price_idr = price_usd * USD_TO_IDR
    return price_usd, price_idr

def create_game_card(game, page, navbar, tabs):
    price_usd = float(game['price']) / 100  
    if price_usd == 0:
        price_text = "Free"
    else:
        _, price_idr = convert_price(price_usd)
        price_text = f"Rp{price_idr:,.0f}".replace(",", ".")

    return ft.Container(
        content=ft.Card(
            color=ft.colors.BLACK26,
            content=ft.Column(
                [
                    ft.Image(src=game["header_image"], fit=ft.ImageFit.CONTAIN),
                    ft.Text(game["name"], size=16, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                    ft.Text(price_text, color=ft.colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ),
        on_click=lambda e, g=game: show_game_details(g, page, navbar, tabs)
    )

def create_game_grid(games, page, navbar, tabs):
    game_cards = [create_game_card(game, page, navbar, tabs) for game in games]
    
    return ft.GridView(
        controls=game_cards,
        max_extent=200,
        spacing=50,
        run_spacing=10
    )

def update_game_grid(games, page, navbar, tabs):
    game_grid.controls = create_game_grid(games, page, navbar, tabs).controls
    page.update()
    
# Inisialisasi game_grid
game_grid = ft.GridView(controls=[], max_extent=200, spacing=50, run_spacing=10)
