if False:
    from lib.Processing3 import *


# 色が変わる四角
def setup():
    size(300, 300)
    strokeWeight(5)
    frameRate(10)


def draw():
    for i in range(0, 150, 10):
        stroke(random(256), random(256), random(256))
        rect(i, i, (300 - i * 2), (300 - i * 2))