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

    def route_change(route):
        page.views.clear()
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
                                #on_click=toggle_theme_button,
                            )
                        ],
                    ),
                    ft.BottomAppBar(
                        bgcolor=ft.colors.GREY,
                        shape=ft.NotchShape.CIRCULAR,
                        content=ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda _: page.go("/calendar")),
                                ft.IconButton(icon=ft.icons.HOME, on_click=lambda _: page.go("/")),
                                ft.IconButton(icon=ft.icons.SETTINGS, on_click=lambda _: page.go("/settings")),
                            ],
                        )
                    )
                ],
            )
        )
        if page.route == "/calendar":
            page.views.append(
                ft.View(
                    "/calendar",
                    [
                        ft.AppBar(title=ft.Text("Calendar"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.BottomAppBar(
                        bgcolor=ft.colors.GREY,
                        shape=ft.NotchShape.CIRCULAR,
                        content=ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda _: page.go("/calendar")),
                                ft.IconButton(icon=ft.icons.HOME, on_click=lambda _: page.go("/")),
                                ft.IconButton(icon=ft.icons.SETTINGS, on_click=lambda _: page.go("/settings")),
                            ],
                        )
                    )
                    ],
                )
            )
        if page.route == "/settings":
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
                        bgcolor=ft.colors.GREY,
                        shape=ft.NotchShape.CIRCULAR,
                        content=ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.icons.CALENDAR_MONTH, on_click=lambda _: page.go("/calendar")),
                                ft.IconButton(icon=ft.icons.HOME, on_click=lambda _: page.go("/")),
                                ft.IconButton(icon=ft.icons.SETTINGS, on_click=lambda _: page.go("/settings")),
                            ],
                        )
                    )
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.add(ft.Text(f"Initial route: {page.route}"))

    page.add(ft.SafeArea(ft.Text("Hello")))

ft.app(target=main)
