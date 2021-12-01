if False:
    from lib.Processing3 import *


def setup():
    size(800, 600)
    frameRate(60)
    background(0)
    noStroke()


def draw():
    for i in range(100):
        x = random(0, width)
        y = random(0, height)
        distance = dist(x, y, width / 2, height / 2)

        if distance < height / 10:
            noStroke()
            fill(63, 127, 255, 100)
        else:
            noFill()
            stroke(31, 127, 255, 100)

        ellipse(x, y, 10, 10)
