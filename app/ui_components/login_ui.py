from flet import *
from ui_components import UserInputField, SignInButton

def login_ui(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#212328"
    
    page.add(
        Card(
            width=320,
            height=300,
            elevation=10,
            content=Container(
                bgcolor="#23262a",
                border_radius=6,
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Divider(height=20, color="transparent"),
                        Text("Login", size=18, weight="bold"),
                        Divider(height=20, color="transparent"),
                        UserInputField(
                            icons.PERSON_ROUNDED,
                            "Email",
                            False,
                            True,
                            False,
                        ),
                        Divider(height=1, color="transparent"),
                        UserInputField(
                            icons.LOCK_OUTLINE_ROUNDED,
                            "Password",
                            True,
                            False,
                            False,
                        ),
                        Divider(height=1, color="transparent"),
                        SignInButton("Sign In"),
                    ],
                ),
            ),
        )
    )
    page.update()
