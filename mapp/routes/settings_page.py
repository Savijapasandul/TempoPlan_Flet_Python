# routes/settings_page.py
import flet as ft

# light theme / dark theme
def toggle_theme_button(e):
    if e.control.selected:
        page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
    else:
        page.theme_mode = ft.ThemeMode.DARK
        page.update()
    e.control.selected = not e.control.selected
    e.control.update()

def settings_page(page):
    # Settings page
    
    page.views.append(
        ft.View(
            "/settings", 
            [
                ft.AppBar(
                    title=ft.Text("Settings"), 
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    actions=[
                        ft.IconButton(
                            icon=ft.icons.LIGHT_MODE,
                            selected_icon=ft.icons.DARK_MODE,
                            style=ft.ButtonStyle(padding=0),
                            selected=False,
                            on_click=toggle_theme_button,
                        ),
                    ],
                ),
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
