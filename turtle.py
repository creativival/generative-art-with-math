if False:
    from lib.Processing3 import *


def forward(length):
    line(0, 0, 0, -length)
    translate(0, -length)


def backward(length):
    line(0, 0, 0, length)
    translate(0, length)


def right_turn(degree):
    rotate(degree)


def left_turn(degree):
    rotate(-degree)


def set_color(r, g=None, b=None, a=None):
    if a is not None:
        stroke(r, g, b, a)
    elif b is not None:
        stroke(r, g, b)
    elif g is not None:
        stroke(r, g)
    else:
        stroke(r)


def pen_down():
    stroke(0)


def pen_up():
    noStroke()


def pen_size(pixel):
    strokeWeight(pixel)


def set_pos(x, y):
    translate(x, y)
