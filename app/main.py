import flet
from flet import *
# from ui_components.login_ui import LoginUI
# from ui_components.new_user_ui import NewUserUI
from ui_components.welcome_ui import WelcomeUI
# from authentication.authentication import handle_create_account

def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#212328"
    
    # Create UI components instances
    # login_ui = LoginUI(page)
    # new_user_ui = NewUserUI(page)
    welcome_ui = WelcomeUI(page)

    # Build UI components
    # login_ui.build()
    # new_user_ui.build()
    welcome_ui.build()

if __name__ == "__main__":
    flet.app(target=main)
