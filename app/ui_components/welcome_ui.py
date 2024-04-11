from flet import *
import random
from math import pi
import time

class WelcomeUI:
    def __init__(self, page: Page):
        self.page = page

    def build(self):
        # Define the UI components for the welcome screen
        self.add_welcome_animation()
        self.page.update()

    def add_welcome_animation(self):
        size = 10
        gap = 2
        duration = 2000

        c1 = colors.PINK_500
        c2 = colors.AMBER_500
        c3 = colors.LIGHT_GREEN_500
        c4 = colors.DEEP_PURPLE_500
        c5 = colors.DEEP_ORANGE_500
        c6 = colors.LIGHT_BLUE_500
        c7 = colors.INDIGO_600

        all_colors = [
            colors.AMBER_400,
            colors.AMBER_ACCENT_400,
            colors.BLUE_400,
            colors.BROWN_400,
            colors.CYAN_700,
            colors.DEEP_ORANGE_500,
            colors.CYAN_500,
            colors.INDIGO_600,
            colors.ORANGE_ACCENT_100,
            colors.PINK,
            colors.RED_600,
            colors.GREEN_400,
            colors.GREEN_ACCENT_200,
            colors.TEAL_ACCENT_200,
            colors.LIGHT_BLUE_500,
        ]

        parts = [
            # W
            (0, 0, c1),
            (0, 1, c1),
            (0, 2, c1),
            (0, 3, c1),
            (0, 4, c1),
            (1, 3, c1),
            (1.5, 2, c1),
            (2, 3, c1),
            (3, 3, c1),
            (3, 2, c1),
            (3, 1, c1),
            (3, 0, c1),
            (3, 4, c1),
            # E
            (5, 0, c2),
            (6, 0, c2),
            (7, 0, c2),
            (5, 1, c2),
            (5, 2, c2),
            (6, 2, c2),
            (7, 2, c2),
            (5, 3, c2),
            (5, 4, c2),
            (6, 4, c2),
            (7, 4, c2),
            # L
            (9, 0, c3),
            (9, 1, c3),
            (9, 2, c3),
            (9, 3, c3),
            (9, 4, c3),
            (10, 4, c3),
            (11, 4, c3),
            # C
            (13, 0, c4),
            (13, 1, c4),
            (13, 2, c4),
            (13, 3, c4),
            (13, 4, c4),
            (14, 0, c4),
            (14, 4, c4),
            (15, 0, c4),
            (15, 4, c4),
            # O
            (17, 0, c5),
            (18, 0, c5),
            (19, 0, c5),
            (17, 1, c5),
            (17, 2, c5),
            (17, 3, c5),
            (17, 4, c5),
            (18, 4, c5),
            (19, 4, c5),
            (19, 3, c5),
            (19, 2, c5),
            (19, 1, c5),    
            # M
            (21, 0, c6),
            (21, 1, c6), 
            (21, 2, c6),
            (21, 3, c6),
            (21, 4, c6),
            (24, 0, c6),
            (24, 1, c6),
            (24, 2, c6),
            (24, 3, c6),
            (24, 4, c6),
            (22, 1, c6),
            (23, 1, c6),
            (22.5, 2, c6),
            # E
            (26, 0, c7),
            (27, 0, c7),
            (28, 0, c7),
            (26, 1, c7),
            (26, 2, c7),
            (27, 2, c7),
            (28, 2, c7),
            (26, 3, c7),
            (26, 4, c7),
            (27, 4, c7),
            (28, 4, c7),
        ]

        width = 100 * (size + gap)
        height = 30 * (size + gap)

        # spread parts randomly
        for i in range(len(parts)):
            canvas.controls.append(
                Container(
                    animate=duration,
                    animate_position=duration,
                    animate_rotation=duration,
                )
            )

        canvas = Stack(
            width=width,
            height=height,
            animate_scale=duration,
            animate_opacity=duration,
        )
        
        go_button = ElevatedButton("Go!", on_click=assemble, visible=True)
        again_button = ElevatedButton("Again!", on_click=randomize, visible=False)
        
        def randomize(e):
            random.seed()
            for i in range(len(parts)):
                c = canvas.controls[i]
                part_size = random.randrange(int(size / 2), int(size * 3))
                c.left = random.randrange(0, width)
                c.top = random.randrange(0, height)
                c.bgcolor = all_colors[random.randrange(0, len(all_colors))]
                c.width = part_size
                c.height = part_size
                c.border_radius = random.randrange(0, int(size / 2))
                c.rotate = random.randrange(0, 90) * 2 * pi / 360
            canvas.scale = 5
            canvas.opacity = 0.3
            go_button.visible = True
            again_button.visible = False
            self.page.update()

        def assemble(e):
            i = 0
            for left, top, bgcolor in parts:
                c = canvas.controls[i]
                c.left = left * (size + gap)
                c.top = top * (size + gap)
                c.bgcolor = bgcolor
                c.width = size
                c.height = size
                c.border_radius = 5
                c.rotate = 0
                i += 1
            canvas.scale = 1
            canvas.opacity = 1
            go_button.visible = False
            again_button.visible = True
            self.page.update()

        randomize(None)

        canvas_container = Container(
            expand=True,
            alignment=alignment.center,
            content=Column(
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                tight=True,
                controls=[
                    canvas,
                    go_button,
                    again_button,
                ],
            ),
        )

        self.page.add(canvas_container)

# Usage
if __name__ == "__main__":
    app(target=lambda page: WelcomeUI(page).build())
