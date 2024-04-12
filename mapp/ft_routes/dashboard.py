from flet import *

class Dashboard:
    def __init__(self, page: Page):
        self.page = page

    def build(self):
        # Define the UI components for the welcome screen
        self.page.add(Text("Welcome"))
        self.page.update()
