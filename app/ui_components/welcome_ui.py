from flet import *

class WelcomeUI:
    def __init__(self, page: Page):
        self.page = page

    def build(self):
        # Define the UI components for the welcome screen
        self.page.add(Text("Welcome UI"))
        self.page.update()
