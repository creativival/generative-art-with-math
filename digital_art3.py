if False:
    from lib.Processing3 import *

# 円運動する楕円
import random

count = 0.0
d_range = 0.9


def setup():
    size(300, 300)
    noStroke()
    colorMode(HSB, 100)
    frameRate(10)


def draw():
    background(0)
    global count

    for i in range(0, 100, 10):
        start_angle = count % 360
        angle = radians(i * 360 / 100 + start_angle)
        x = 150 + cos(angle) * 100
        y = 150 - sin(angle) * 100
        dx = 50 * random_range(d_range)
        dy = 50 * random_range(d_range)

        fill(i, 80, 100)
        ellipse(x, y, dx, dy)

    count = count + 6


def random_range(r):
    return random.uniform(r, 1 / r)
