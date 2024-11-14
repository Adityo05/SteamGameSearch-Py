import flet as ft
import threading

def create_carousel():
    carousel_images = [
        "D:\Dokumen\Semester 2\Struktur Data\Projek searching v2\Banner\desktop_english.jpeg",
        "D:\Dokumen\Semester 2\Struktur Data\Projek searching v2\Banner\deck_banner_lcd_static_desktop_english.jpeg",
        "D:\Dokumen\Semester 2\Struktur Data\Projek searching v2\Banner\deck_banner_animated_static_english.jpeg",
    ]
    current_image_index = 0
    image_container = ft.Container(
        width=800,
        height=200,
        content=ft.Image(src=carousel_images[current_image_index], fit=ft.ImageFit.CONTAIN),
        opacity=1.0,
        animate_opacity=300  
    )

    def update_carousel():
        nonlocal current_image_index
        current_image_index = (current_image_index + 1) % len(carousel_images)
        image_container.content.src = carousel_images[current_image_index]
        image_container.update()

    def fade_out():
        image_container.opacity = 0.0
        image_container.update()
        threading.Timer(0.3, update_carousel).start()  # Wait for fade out to complete before updating image
        threading.Timer(0.3, fade_in).start()  # Start fade in after updating image

    def fade_in():
        image_container.opacity = 1.0
        image_container.update()
        schedule_next_slide()

    def schedule_next_slide():
        threading.Timer(5.0, fade_out).start()

    def next_image(e=None):
        fade_out()

    def previous_image(e=None):
        nonlocal current_image_index
        current_image_index = (current_image_index - 1) % len(carousel_images)
        image_container.content.src = carousel_images[current_image_index]
        image_container.update()

    schedule_next_slide()

    return ft.Row(
        controls=[
            ft.IconButton(icon=ft.icons.CHEVRON_LEFT, on_click=previous_image),
            image_container,
            ft.IconButton(icon=ft.icons.CHEVRON_RIGHT, on_click=next_image),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

def main(page: ft.Page):
    page.title = "Carousel Example"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(create_carousel())