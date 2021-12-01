if False:
    from lib.Processing3 import *


def setup():
    size(800, 600)
    y = 60
    d = 80
    interval_x = 10
    interval_y = 1
    interval_z = 100

    for j in range(10):
        for i in range(100):
            ellipse(75 + interval_x * i, y + interval_y * i + interval_z * j, d, d)
