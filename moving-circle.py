if False:
    from lib.Processing3 import *


def setup():
    size(800, 600)


def draw():
    if mousePressed:
        fill(0)
    else:
        fill(255)

    ellipse(mouseX, mouseY, 80, 80)
