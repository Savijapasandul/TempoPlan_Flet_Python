# routes/home.py
import flet as ft

# notifications    
def toggle_notification_button(e):
    if e.control.selected:
        page.update()
    else:
        page.update()
    e.control.selected = not e.control.selected
    e.control.update()

def home_page(page):
    # Home page code here
    page.views.append(
        ft.View(
            "/", 
            [
                ft.AppBar(
                    title=ft.Text("Home"), 
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    actions=[
                        ft.IconButton(
                            icon=ft.icons.NOTIFICATIONS, 
                            selected_icon=ft.icons.NOTIFICATIONS_ACTIVE_ROUNDED,
                            style=ft.ButtonStyle(padding=0),
                            selected=False,
                            on_click=toggle_notification_button,
                        )
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
