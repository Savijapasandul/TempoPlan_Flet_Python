# routes/calendar_page.py
import flet as ft

def calendar_page(page):
    # Calendar page
    page.views.append(
        ft.View(
            "/calendar", 
            [
                ft.AppBar(title=ft.Text("Calendar"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.BottomAppBar(
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    shape=ft.NotchShape.CIRCULAR,
                    content=ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.icons.CALENDAR_MONTH, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/calendar")),
                            ft.IconButton(icon=ft.icons.HOME, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/")),
                            ft.IconButton(icon=ft.icons.SETTINGS, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/settings")),
                        ],
                    )
                )
            ],
        )
    )
