from flet import *
from ui_components.login_ui import UserInputField, SignInButton

class LoginUI:
    def __init__(self, page: Page):
        self.page = page

    def build(self):
        login_ui(self.page)

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
                            icon=icons.PERSON_ROUNDED,
                            label="Email",
                            password=False,
                            autofocus=True,
                            multiline=False,
                        ),
                        Divider(height=1, color="transparent"),
                        UserInputField(
                            icon=icons.LOCK_OUTLINE_ROUNDED,
                            label="Password",
                            password=True,
                            autofocus=False,
                            multiline=False,
                        ),
                        Divider(height=1, color="transparent"),
                        SignInButton(label="Sign In"),
                    ],
                ),
            ),
        )
    )
    page.update()
