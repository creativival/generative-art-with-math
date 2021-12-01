if False:
    from lib.Processing3 import *

import turtle


def setup():
    size(800, 600)
    background(255)
    translate(width / 2, height / 2)

    turtle.pen_size(4)
    turtle.set_color(0, 0, 0)
    turtle.forward(100)
    turtle.right_turn(radians(120))
    turtle.pen_size(8)
    turtle.set_color(64, 0, 0)
    turtle.forward(100)
    turtle.right_turn(radians(120))
    turtle.pen_size(16)
    turtle.set_color(128, 0, 0, 128)
    turtle.forward(100)
