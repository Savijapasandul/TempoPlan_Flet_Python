# modules
import flet as ft
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# main page
def main(page):

    # supabase
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    # page settings
    page.title = "RoomReservePro"
    page.adaptive = True
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    
    # Search handler for available rooms
    def fetch_available_rooms():
        # Query the database to fetch available rooms
        response = supabase.table("rooms").select("*").eq("available_for_booking", True).execute()
        # Check if the response is successful
        available_rooms = response.data
        return available_rooms
        page.update()
        
        
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

    def handle_search_change(e):
        print("on_change data : " + str(e.data))

    # route handler
    def route_change(route):
    
        page.views.clear()    
        page.views.append(
            ft.View(
                # home page
                "/",
                controls=[
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
                        selected_index=0,
                        animation_duration=300,
                        expand=1,
                        tabs=[
                            ft.Tab(
                                text="Active",
                                content=ft.Container(
                                    margin=10,
                                    content=ft.Column(
                                        wrap=True,
                                        expand=True,
                                        width=page.window_width,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text("No bookings yet"),
                                            ft.Text("Sign in or create an account to get started."),
                                            ft.TextButton(text="Log in"),
                                        ]
                                    )  
                                )
                            ),
                            ft.Tab(
                                text="Past",
                                content=ft.Container(
                                    margin=10,
                                    content=ft.Column(
                                        wrap=True,
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=10,
                                        width=page.window_width,
                                        scroll=ft.ScrollMode.AUTO,
                                        controls=[
                                            ft.Text("No pass bookings"),
                                            ft.Text("Sign in or create an account to get started."),
                                            ft.TextButton(text="Log in"),
                                        ]
                                    )
                                ),
                            ),
                            ft.Tab(
                                text="Cancelled",
                                content=ft.Container(
                                    margin=10,
                                    content=ft.Column(
                                        wrap=True,
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=10,
                                        width=page.window_width,
                                        scroll=ft.ScrollMode.AUTO,
                                        controls=[
                                            ft.Text("No cancelled bookings"),
                                            ft.Text("Sign in or create an account to get started."),
                                            ft.TextButton(text="Log in"),
                                        ]
                                    )
                                ),
                            ),
                        ],
                    )
                ],
            )
        )
        if page.route == "/search":
            # Fetch available rooms from Supabase
            rooms = fetch_available_rooms()
            print("Fetched rooms:", rooms)

            # Create controls to display available rooms on the search page
            room_controls = []
            for room in rooms:
                room_controls.append(
                    ft.ListTile(
                        title=ft.Text(room['name']),
                        subtitle=ft.Text(room['description']),
                    )
                )

            page.views.append(
                ft.View(
                    # search page
                    "/search",
                    controls=[
                        ft.AppBar(title=ft.Text("Search"), bgcolor=ft.colors.SURFACE_VARIANT),
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

                        ft.Row(
                            width=page.window_width,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.SEARCH,
                                ),
                                ft.TextField(
                                    hint_text="Search...",
                                ),
                            ]
                        ),
                        ft.Column(
                            scroll=ft.ScrollMode.AUTO,
                            width=page.window_width,
                            controls=room_controls,
                        ),
                    ],
                )
            )

        if page.route == "/room_booking":
            page.views.append(
                ft.View(
                    # notifications page
                    "/room_booking",
                    controls=[
                        ft.AppBar(title=ft.Text("Room Booking"), bgcolor=ft.colors.SURFACE_VARIANT),

                        ft.Container(
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("Room Booking"),
                                    
                                ]
                            )
                        ),
                    ],
                )
            )
        if page.route == "/room_details":
            page.views.append(
                ft.View(
                    # notifications page
                    "/room_details",
                    controls=[
                        ft.AppBar(title=ft.Text("Room Details"), bgcolor=ft.colors.SURFACE_VARIANT),

                        ft.Container(
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("Room Details"),
                                    
                                ]
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
                    controls=[
                        ft.AppBar(title=ft.Text("Notifications"), bgcolor=ft.colors.SURFACE_VARIANT),

                        ft.Container(
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("You don't have any notifications"),
                                    ft.Text("Notifications let you quickly take actions on upcoming or current bookings.") 
                                ]
                            )
                        ),
                    ],
                )
            )

        if page.route == "/login":
            page.views.append(
                ft.View(
                    # login page
                    "/login",
                    controls=[
                        ft.AppBar(title=ft.Text("Login"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Container(
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.TextField(hint_text="Username",),
                                    ft.TextField(hint_text="Password",),
                                    ft.TextButton("Login"),
                                    ft.Text("No account then create a new account"),
                                    ft.TextButton("Create account", on_click=lambda _: page.go("/create_account"))
                                ]
                            )
                        ),
                    ],
                )
            )

        if page.route == "/create_account":
            page.views.append(
                ft.View(
                    # create_account page
                    "/create_account",
                    controls=[
                        ft.AppBar(title=ft.Text("Create Account"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Container(
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.TextField(hint_text="Email address",),
                                    ft.TextField(hint_text="Username",),
                                    ft.TextField(hint_text="Password",),
                                    ft.TextButton("Create account",)
                                ]
                            )
                        ),
                    ],
                )
            )

        if page.route == "/settings":
            is_light_mode = page.theme_mode == ft.ThemeMode.LIGHT
            page.views.append(
                ft.View(
                    # setting page
                    "/settings",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("Settings"), 
                            bgcolor=ft.colors.SURFACE_VARIANT,
                            actions=[
                                ft.IconButton(
                                    icon=ft.icons.DARK_MODE,
                                    selected_icon=ft.icons.LIGHT_MODE,
                                    style=ft.ButtonStyle(padding=0),
                                    selected=is_light_mode,
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

                        ft.Container(
                            content=ft.Column(
                                width=500,
                                scroll=ft.ScrollMode.AUTO,
                                controls=[
                                    ft.Text("Not logged in!"),
                                    ft.TextButton("Log in", on_click=lambda _: page.go("/login")),
                                    ft.ListTile(
                                        leading=ft.Icon(ft.icons.SETTINGS),
                                        trailing=ft.PopupMenuButton(
                                            icon=ft.icons.MORE_VERT,
                                            items=[
                                                ft.PopupMenuItem(text="Item 1"),
                                                ft.PopupMenuItem(text="Item 2"),
                                            ]
                                        ),
                                        title=ft.Text("No implemented setting yet")
                                    ),
                                    ft.ListTile(
                                        leading=ft.Icon(ft.icons.SETTINGS),
                                        title=ft.Text("No implemented setting yet")
                                    ),
                                    ft.ListTile(
                                        leading=ft.Icon(ft.icons.SETTINGS),
                                        title=ft.Text("No implemented setting yet")
                                    ),
                                    ft.ListTile(
                                        leading=ft.Icon(ft.icons.SETTINGS),
                                        title=ft.Text("No implemented setting yet")
                                    ),
                                ]
                            ),
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
