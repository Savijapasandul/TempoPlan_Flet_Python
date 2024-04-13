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
            ),
            ft.IconButton(
                icon=ft.icons.NOTIFICATIONS, 
                selected_icon=ft.icons.NOTIFICATIONS_ACTIVE_ROUNDED,
                style=ft.ButtonStyle(padding=0),
                selected=False,
                #on_click=toggle_theme_button,
            )
        ],
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.CALENDAR_MONTH, label="Calendar"),
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.icons.SETTINGS, label="Settings"),
        ],
        on_change=[
            lambda e: page.go("/calendar"),
            lambda e: page.go("/"),
            lambda e: page.go("/settings"),
        ],
        border=ft.Border(
            top=ft.BorderSide(color=ft.cupertino_colors.SYSTEM_GREY2, width=0)
        ),
    )

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"New route: {e.route}"))

    page.on_route_change = route_change
    page.add(ft.Text(f"Initial route: {page.route}"))

    page.add(ft.SafeArea(ft.Text("Hello")))

ft.app(target=main)
