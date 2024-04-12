# modules
import flet
from flet import *
from ft_routes.dashboard import Dashboard

def main(page: Page):
    page.title = 'TempoRoomPlan'
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "black"
    page.update()
    
    # instances
    dashboard = Dashboard(page)  

    # Build components
    dashboard.build()  

if __name__ == "__main__":
    flet.app(target=main)
