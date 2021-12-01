if False:
    from lib.Processing3 import *

# 円運動する虹
count = 0


def setup():
    size(300, 300)
    noStroke()
    colorMode(HSB, 100)
    frameRate(60)


def draw():
    global count

    for i in range(0, 100):
        start_angle = count % 360
        angle = radians(i * 360 / 100 + start_angle)
        x = 150 + cos(angle) * 100
        y = 150 - sin(angle) * 100

        fill(i, 80, 100)
        ellipse(x, y, 50, 50)

    count = count + 1
