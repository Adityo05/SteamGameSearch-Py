import flet as ft
from carousel import create_carousel
from game_grid import game_grid

def create_footer():
    return ft.Container(
        content=ft.Column(
            controls=[
                # ft.Text("Ryan | Adityo Dwi Saputro | Muhammad Luthfi Firdaus | Hafidz Syahdi Ismallah | Muhammad Adli Barryananda",size=12,color=ft.colors.WHITE),
                ft.Text("Follow us on:", size=12, color=ft.colors.WHITE),
                ft.Row(
                    controls=[
                        ft.IconButton(icon=ft.icons.DISCORD, url="https://discord.gg/PX42qkVgpm"),
                        ft.Text("Discord",size=12,color=ft.colors.WHITE),
                        ft.IconButton(
                                    content=ft.Image(
                                        src="https://img.icons8.com/?size=100&id=WDlIZj1YGQtm&format=png&color=FFFFFF",
                                        width=25,  
                                        height=25
                                    ),
                                    url="https://www.instagram.com/ad.dwisaputro/",  
                        ),
                        ft.Text("Instagram",size=12,color=ft.colors.WHITE),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Text("Politeknik Negeri Pontianak, Jl. Jenderal Ahmad Yani, Bansir Laut,",size=12,color=ft.colors.WHITE),
                ft.Text("Kec. Pontianak Tenggara, Kota Pontianak, Kalimantan Barat 78124, Indonesia",size=12,color=ft.colors.WHITE),
                ft.Text("Copyright © Kelompok 2 2024 | Privacy notice | Terms of use",size=12,color=ft.colors.WHITE)    
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        padding=ft.padding.all(20),
        width=2000,
        bgcolor=ft.colors.BLACK45,
        expand=False
    )

def create_home_content(game_data):
    return ft.Container(
        content=ft.Column(
            controls=[
                create_carousel(),
                game_grid,
                create_footer() 
            ],
            scroll="auto",
            expand=True
        ),
        expand=True,
    )

# def create_home_content(game_data):
#     return ft.Container(
#         content=ft.Column(
#             controls=[
#                 create_carousel(),
#                 game_grid
#             ],
#             scroll="auto",
#             expand=True
#         ),
#         expand=True
#     )
