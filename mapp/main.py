# modules
import flet as ft

def main(page):

    page.adaptive = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    
    def toggle_theme_button(e):
        if e.control.selected:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.update()
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.update()
        e.control.selected = not e.control.selected
        e.control.update()

    page.appbar = ft.AppBar(
        actions=[
            ft.IconButton(
                icon=ft.icons.LIGHT_MODE, 
                selected_icon=ft.icons.DARK_MODE,
                style=ft.ButtonStyle(padding=0),
                selected=False,
                on_click=toggle_theme_button,
            )
        ],
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.NOTIFICATIONS, selected_icon=ft.icons.NOTIFICATIONS_ACTIVE_ROUNDED, label="Notification"),
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.icons.SETTINGS, label="Settings",
            ),
        ],
        border=ft.Border(
            top=ft.BorderSide(color=ft.cupertino_colors.SYSTEM_GREY2, width=0)
        ),
    )

    page.add(
        ft.SafeArea( ft.Text("Hello"))
    )


ft.app(target=main)