# main.py

# modules
from flet import flet, UserControl, Page
#, Column, Row, Container, Text, padding, alignment

# main class
class Dashboard(UserControl):
    def build(self):
        return Column(
            controls=[]
        )

def start (page: Page):
    page.title = 'TempoRoomPlan'
    page.horizontal_alignment = 'Center'
    page.vertical_alignment = 'Center'

    app = Dashboard()
    page.add(app)
    page.update()

if __name__ == "__name__":
    flet.app(target=start)