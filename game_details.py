import flet as ft

def show_game_details(game, page, navbar, tabs):
    def go_back(e):
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

    current_screenshot_index = 0

    def update_screenshot():
        screenshot_image.src = game["screenshots"][current_screenshot_index]
        page.update()

    def next_screenshot(e):
        nonlocal current_screenshot_index
        current_screenshot_index = (current_screenshot_index + 1) % len(game["screenshots"])
        update_screenshot()

    def previous_screenshot(e):
        nonlocal current_screenshot_index
        current_screenshot_index = (current_screenshot_index - 1) % len(game["screenshots"])
        update_screenshot()

    screenshot_image = ft.Image(src=game["screenshots"][current_screenshot_index], fit=ft.ImageFit.CONTAIN)

    detail_content = ft.Column(
        [
            ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=go_back),
            ft.Row(
                [
                    ft.Image(src=game["header_image"], fit=ft.ImageFit.CONTAIN),
                    ft.Column(
                        [
                            ft.Text(game["name"], size=24, weight=ft.FontWeight.BOLD),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            ft.Card(
                color=ft.colors.BLACK45,
                content=ft.Column(
                    [
                        ft.Text(game["description"], size=12, weight=ft.FontWeight.NORMAL, color="white"),
                    ]
                )
            ),
            ft.Row(
                [
                    ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=previous_screenshot),
                    screenshot_image,
                    ft.IconButton(icon=ft.icons.ARROW_FORWARD, on_click=next_screenshot),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        expand=True,
        scroll="auto"  
    )

    scrollable_detail_content = ft.Container(
        content=detail_content,
        expand=True,
        padding=ft.padding.all(10), 
    )
    # scrollable_detail_content = ft.Container(
    #     content=ft.Column(
    #         controls=[detail_content],
    #         scroll="auto",
    #         expand=True
    #     ),
    #     expand=True
    # )

    page.clean()
    page.add(scrollable_detail_content)
    page.update()
