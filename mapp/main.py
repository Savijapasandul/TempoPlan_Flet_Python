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
        response = supabase.table("available_rooms").select("*").eq("available_for_booking", True).execute()
        # Check if the response is successful
        available_rooms = response.data
        return available_rooms
        page.update()
    
    def fetch_account_details():
        response = supabase.table("users").select("*").execute()
        account_details = response.data
        return account_details
        page.update()
                
    def on_create_account_click(email_input, password_input, username_input):
        email = email_input.value
        password = password_input.value
        username = username_input.value
        handler_create_account(email, password, username)
        page.go("/login")
    
    def on_login_click(username_input, password_input):
        username = username_input.value
        password = password_input.value
        login(username, password)
        page.go("/settings")
    
    def handler_create_account(email, password, username):
        data = supabase.table('users').insert({"email": email, "password": password, "username": username}).execute()
        return True
    
    def login(username, password):
        account_details = fetch_account_details()
        for account in account_details:
            if account["username"] == username and account["password"] == password:
                return True
        return False

    def filter_rooms(keyword):
        rooms = fetch_available_rooms()
        filtered_rooms = [room for room in rooms if keyword.lower() in room['name'].lower() or keyword.lower() in room['description'].lower()]
        return filtered_rooms
        
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

    def handle_expansion_tile_change(e):
        if e.control.trailing:
            e.control.trailing.name = (
                ft.icons.ARROW_DROP_DOWN
                if e.control.trailing.name == ft.icons.ARROW_DROP_DOWN_CIRCLE
                else ft.icons.ARROW_DROP_DOWN_CIRCLE
            )
            page.update()

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
            room_controls = []
            for room in rooms:
                room_id = room['id']
                room_controls.append(
                    ft.ExpansionTile(
                        title=ft.Text(room['name']),
                        subtitle=ft.Text(room['description']),
                        trailing=ft.Icon(ft.icons.ARROW_DROP_DOWN),
                        on_change=handle_expansion_tile_change,
                        controls=[
                            ft.ListTile(title=ft.TextField(label="Starting Time", border="none", hint_text="YYYY-MM-DD HH:MM:SS+TZ")),
                            ft.ListTile(title=ft.TextField(label="Ending Time", border="none", hint_text="YYYY-MM-DD HH:MM:SS+TZ")),
                            ft.ListTile(title=ft.TextField(label="Username", border="none", hint_text="Enter Username here")),
                            ft.ListTile(title=ft.ElevatedButton("Book")),
                        ],
                    )
                ),
                
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
                        ft.Tabs(
                            selected_index=0,
                            animation_duration=300,
                            expand=1,
                            tabs=[
                                ft.Tab(
                                    icon=ft.icons.SEARCH,
                                    content=ft.Container(                                    
                                        margin=10,
                                        content=ft.Column(
                                            expand=True,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=10,
                                            width=page.window_width,
                                            scroll=ft.ScrollMode.AUTO,
                                            controls=[
                                                ft.Container(
                                                    content=ft.Column(
                                                        [
                                                            ft.TextField(label="Search",border="none",hint_text="Enter text here",),
                                                            ft.ProgressBar(width=page.window_width,color="blue")
                                                        ]
                                                    ),
                                                ),
                                                ft.Divider(),
                                                ft.Container(
                                                    content=ft.Column(
                                                        controls=room_controls,
                                                    ),
                                                )
                                            ]
                                        )
                                    ),
                                ),
                                ft.Tab(
                                    text="All available rooms",
                                    content=ft.Container(
                                        margin=10,
                                        content=ft.Column(
                                            expand=True,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=10,
                                            width=page.window_width,
                                            scroll=ft.ScrollMode.AUTO,
                                            controls=room_controls,
                                        )
                                    ),
                                ),
                            ],
                        )
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
            login_username = ft.TextField(label="Username")
            login_password = ft.TextField(label="Password", password=True, can_reveal_password=True)
            page.views.append(
                ft.View(
                    # login page
                    "/login",
                    controls=[
                        ft.AppBar(title=ft.Text("Login"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Container(
                            margin=10,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("Login with your account details"),
                                    login_username,    
                                    login_password,
                                    ft.TextButton("Login", on_click=lambda _: on_login_click(login_username, login_password)),
                                    ft.Text("Don't have an account? ", spans=[ft.TextSpan("Sign Up", ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, color=ft.colors.BLUE), on_click=lambda _: page.go("/create_account"))])
                                ]
                            )
                        ),
                    ],
                )
            )

        if page.route == "/create_account":
            email_input = ft.TextField(label="Email address")
            username_input = ft.TextField(label="Username")
            password_input = ft.TextField(label="Password", password=True, can_reveal_password=True)
            page.views.append(
                ft.View(
                    # create_account page
                    "/create_account",
                    controls=[
                        ft.AppBar(title=ft.Text("Create Account"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Container(
                            margin=10,
                            content=ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.Text("Sign up of an account"),
                                    email_input,
                                    username_input,
                                    password_input,
                                    ft.TextButton("Create account", on_click=lambda _: on_create_account_click(email_input, password_input, username_input)),
                                    ft.Text("Already have an account? ", spans=[ft.TextSpan("Log In", ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE, color=ft.colors.BLUE), on_click=lambda _: page.go("/login"))])
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
