# modules
import flet as ft

# main page
def main(page):

    # page settings
    page.title = "RoomReservePro"
    page.adaptive = True
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    
    # light theme / dark theme
    def toggle_theme_button(e):
        if e.control.selected:
            page.theme_mode = ft.ThemeMode.DARK
            page.update()
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.update()
        e.control.selected = not e.control.selected
        e.control.update()

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
                                on_click=lambda _: page.go("/notifications"),
                                adaptive=True,
                            )
                        ],
                    ),

                    ft.BottomAppBar(
                        bgcolor=ft.colors.SURFACE_VARIANT,
                        shape=ft.NotchShape.CIRCULAR,
                        content=ft.Row(
                            spacing=50,
                            width=page.window_width,
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                            controls=[
                                ft.IconButton(icon=ft.icons.SEARCH, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/search"), adaptive=True),
                                ft.IconButton(icon=ft.icons.HOME, selected=True, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/"), adaptive=True),
                                ft.IconButton(icon=ft.icons.SETTINGS, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/settings"), adaptive=True),
                            ],
                        )
                    ),

                    ft.Tabs(
                        selected_index=1,
                        animation_duration=300,
                        expand=1,
                        tabs=[
                            ft.Tab(
                                text="Active",
                                content=ft.Container(
                                    margin=5,
                                    content=ft.Row(
                                        width=page.window_width,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    )  
                                )
                            ),
                            ft.Tab(
                                text="Past",
                                content=ft.Container(
                                    margin=5,
                                    content=ft.Row(
                                        wrap=True,
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                        spacing=10,
                                        width=page.window_width,
                                        #controls=active_home_tab,
                                        scroll=ft.ScrollMode.AUTO,
                                    )
                                ),
                            ),
                            ft.Tab(
                                text="Cancelled",
                                content=ft.Container(
                                    margin=5,
                                    content=ft.Row(
                                        wrap=True,
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                        spacing=10,
                                        width=page.window_width,
                                        #controls=available_tab_items,
                                        scroll=ft.ScrollMode.AUTO,
                                    )
                                ),
                            ),
                        ],
                    )
                ],
            )
        )
        if page.route == "/search":
            page.views.append(
                ft.View(
                    # calendar page
                    "/search",
                    [
                        ft.AppBar(title=ft.Text("Search"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.BottomAppBar(
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            shape=ft.NotchShape.CIRCULAR,
                            content=ft.Row(
                                spacing=50,
                                width=page.window_width,
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                controls=[
                                    ft.IconButton(icon=ft.icons.SEARCH, selected=True, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/search"), adaptive=True),
                                    ft.IconButton(icon=ft.icons.HOME, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/"), adaptive=True),
                                    ft.IconButton(icon=ft.icons.SETTINGS, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/settings"), adaptive=True),
                                ],
                            )
                        ),
                    ],
                )
            )
        if page.route == "/notifications":
            page.views.append(
                ft.View(
                    # notifications page
                    "/notifications",
                    [
                        ft.AppBar(title=ft.Text("Notifications"), bgcolor=ft.colors.SURFACE_VARIANT),
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
                                    icon=ft.icons.DARK_MODE,
                                    selected_icon=ft.icons.LIGHT_MODE,
                                    style=ft.ButtonStyle(padding=0),
                                    selected=False,
                                    on_click=toggle_theme_button,
                                    adaptive=True,
                                ),
                            ],
                        ),
                        ft.BottomAppBar(
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            shape=ft.NotchShape.CIRCULAR,
                            content=ft.Row(
                                spacing=50,
                                width=page.window_width,
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                controls=[
                                    ft.IconButton(icon=ft.icons.SEARCH, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/search"), adaptive=True),
                                    ft.IconButton(icon=ft.icons.HOME, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/"), adaptive=True),
                                    ft.IconButton(icon=ft.icons.SETTINGS, selected=True, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/settings"), adaptive=True),
                                ],
                            )
                        ),
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
