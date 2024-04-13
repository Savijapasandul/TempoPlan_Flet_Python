# modules
import flet as ft

# main page
def main(page):

    # page settings
    page.adaptive = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    
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

    # notifications    
    def toggle_notification_button(e):
        if e.control.selected:
            page.update()
        else:
            page.update()
        e.control.selected = not e.control.selected
        e.control.update()

    # bottom bar
    bottom_app_bar = ft.BottomAppBar(
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

    # route handler
    def route_change(route):
    
        page.views.clear()    
        page.views.append(
            ft.View(
                # home page
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
                    bottom_app_bar
                ],
            )
        )
        if page.route == "/calendar":
            page.views.append(
                ft.View(
                    # calendar page
                    "/calendar",
                    [
                        ft.AppBar(title=ft.Text("Calendar"), bgcolor=ft.colors.SURFACE_VARIANT),
                        bottom_app_bar
                    ],
                )
            )
        if page.route == "/settings":
            page.views.append(
                ft.View(
                    # setting page
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
                        bottom_app_bar
                    ],
                )
            )
        page.update()

    # page view
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)
