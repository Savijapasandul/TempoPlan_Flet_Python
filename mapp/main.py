# modules
import flet as ft

# main page
def main(page):

    # page settings
    page.title = "TempoRoomPlan"
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
    
    def booked_tab(rooms):
        items = []
        for room in rooms:
            items.append(
                ft.Container(
                    content=ft.Text(value=f"Room {room['number']}"),
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    border_radius=ft.border_radius.all(5),
                )
            )
        return items

    def available_tab(rooms):
        items = []
        for room in rooms:
            items.append(
                ft.Container(
                    content=ft.Text(value=f"Room {room['number']}"),
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    border_radius=ft.border_radius.all(5),
                )
            )
        return items


    def close_anchor(e):
        text = f"Color {e.control.data}"
        print(f"closing view from {text}")
        anchor.close_view(text)

    def handle_change(e):
        print(f"handle_change e.data: {e.data}")

    def handle_submit(e):
        print(f"handle_submit e.data: {e.data}")

    def handle_tap(e):
        print(f"handle_tap")

    anchor = ft.SearchBar(
        view_elevation=4,
        divider_color=ft.colors.AMBER,
        bar_hint_text="Search colors...",
        view_hint_text="Choose a color from the suggestions...",
        on_change=handle_change,
        on_submit=handle_submit,
        on_tap=handle_tap,
        controls=[
            ft.ListTile(title=ft.Text(f"Color {i}"), on_click=close_anchor, data=i)
            for i in range(10)
        ],
    )

    # Sample room details
    booked_rooms = [
        {"number": 101, "status": "Booked", "guest": "John Doe"},
        {"number": 102, "status": "Booked", "guest": "Jane Smith"},
    ]
    available_rooms = [
        {"number": 201, "status": "Available"},
        {"number": 202, "status": "Available"},
    ]

    booked_tab_items = booked_tab(booked_rooms)
    available_tab_items = available_tab(available_rooms)

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
                                ft.IconButton(icon=ft.icons.CALENDAR_MONTH, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/calendar"), adaptive=True),
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
                                tab_content=ft.Icon(ft.icons.SEARCH),
                                content=ft.Container(
                                    margin=5,
                                    content=ft.Row(
                                        width=page.window_width,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            anchor,
                                            ft.OutlinedButton("Open Search View", on_click=lambda _: anchor.open_view(),),
                                            
                                        ],
                                    )  
                                )
                            ),
                            ft.Tab(
                                text="Booked",
                                icon=ft.icons.MEETING_ROOM,
                                content=ft.Container(
                                    margin=5,
                                    content=ft.Row(
                                        wrap=True,
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                        spacing=10,
                                        width=page.window_width,
                                        controls=booked_tab_items,
                                        scroll=ft.ScrollMode.AUTO,
                                    )
                                ),
                            ),
                            ft.Tab(
                                text="Available",
                                icon=ft.icons.EVENT_AVAILABLE,
                                content=ft.Container(
                                    margin=5,
                                    content=ft.Row(
                                        wrap=True,
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                        spacing=10,
                                        width=page.window_width,
                                        controls=available_tab_items,
                                        scroll=ft.ScrollMode.AUTO,
                                    )
                                ),
                            ),
                        ],
                    )
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
                        ft.BottomAppBar(
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            shape=ft.NotchShape.CIRCULAR,
                            content=ft.Row(
                                spacing=50,
                                width=page.window_width,
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                controls=[
                                    ft.IconButton(icon=ft.icons.CALENDAR_MONTH, selected=True, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/calendar"), adaptive=True),
                                    ft.IconButton(icon=ft.icons.HOME, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/"), adaptive=True),
                                    ft.IconButton(icon=ft.icons.SETTINGS, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/settings"), adaptive=True),
                                ],
                            )
                        ),
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
                                    ft.IconButton(icon=ft.icons.CALENDAR_MONTH, style=ft.ButtonStyle(padding=0), on_click=lambda _: page.go("/calendar"), adaptive=True),
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
