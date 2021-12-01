if False:
    from lib.Processing3 import *

import turtle

interval_x = 200
interval_y = 150


def setup():
    size(800, 600)
    background(255)
    translate(width / 2 - interval_x, height / 2 - interval_y)

    for k in range(3):
        for j in range(3):
            for i in range(120):
                pushMatrix()
                turtle.set_pos(j * interval_x, k * interval_y)
                degree = radians(i * 3)
                turtle.pen_size(1)
                turtle.set_color(255, 0, 0)
                turtle.right_turn(degree)
                turtle.forward(150)
                popMatrix()
