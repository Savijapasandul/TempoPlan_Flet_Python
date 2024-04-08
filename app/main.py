# modules
import flet 
from flet import *
import time 
from math import pi

# Animated boxes
class AnimatedBox(UserControl):
    def __init__(self, border_color, bg_color, rotate_angle):
        # instances for each parameter
        self.border_color = border_color
        self.bg_color = bg_color
        self.rotate_angle = rotate_angle
        super().__init__()

    def build(self):
        return Container(
            width=80,
            height=80,
            border=border.all(2.5, self.border_color),
            bgcolor=self.bg_color,
            border_radius=2,
            rotate=transform.Rotate(self.rotate_angle, alignment.center),
            animate_rotation=animation.Animation(700, "easeInOut"),
        )

def main(page: Page):
    # dimensions
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.bgcolor = '#1f262f'

    # Animate red_box
    def animate_red_box():
        ccw_rotation = -pi / 4  # Changed to counterclockwise rotation
        red_box = page.controls[0].content.content.controls[1].controls[0].controls[0]
        # Counter
        counter = 0
        while True:
            # rotate 4x before switching directions
            if counter >= 0 and counter <= 4:
                red_box.rotate = transform.Rotate(ccw_rotation, alignment.center)
                red_box.update()
                ccw_rotation -= pi / 2
                counter += 1
                time.sleep(0.7)
            # reverse directions
            if counter >= 5 and counter <= 10:
                red_box.rotate = transform.Rotate(ccw_rotation, alignment.center)
                ccw_rotation += pi / 2
                red_box.update()
                counter += 1
                time.sleep(0.7)
            # reset counter
            elif counter >= 10:
                counter = 0

    # Animate blue_box
    def animate_blue_box():
        cw_rotation = pi / 4  # Changed to clockwise rotation
        blue_box = page.controls[0].content.content.controls[1].controls[0].controls[1]  # Adjusted to access blue box
        # Counter
        counter = 0
        while True:     
            if counter >= 0 and counter <= 4:        
                blue_box.rotate = transform.Rotate(cw_rotation, alignment.center)    
            blue_box.update()
            cw_rotation -= pi / 2  # Adjusted for counterclockwise rotation
            counter += 1
            time.sleep(0.7)
            # reverse directions
            if counter >= 5 and counter <= 10:
                blue_box.rotate = transform.Rotate(cw_rotation, alignment.center)    
                cw_rotation += pi / 2  # Adjusted for counterclockwise rotation
                blue_box.update()
                counter += 1
                time.sleep(0.7)
            # reset counter
            elif counter >= 10:
                counter = 0

    # main page controls 
    page.add(
        Card(
            width=400,
            height=700,
            elevation=15,
            content=Container(
                bgcolor='#23262a',
                border_radius=6,
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        # Main control code
                        Divider(
                            height=40,
                            color='transparent'
                        ),
                        Stack(
                            controls=[
                                # pass animated box class & recall class
                                AnimatedBox("#e9665a", None, 0),
                                AnimatedBox("#7df6dd", "#23262a", pi / 4),
                            ]
                        ),
                    ],
                ),
            ),
        )
    )

    page.update()
    animate_red_box()
    animate_blue_box()

if __name__ == "__main__":
    flet.app(target=main)
