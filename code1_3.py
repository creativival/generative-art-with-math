if False:
    from lib.Processing3 import *

"""
長方形の分割によるユークリッド互除法の可視化（彩色）
"""

SIZE_X = 800
SIZE_Y = 800
SCALAR = 50
NUM_A = SCALAR * 7
NUM_B = SCALAR * 16
wd = NUM_B
position = PVector(0, 0)


def setup():
    global wd
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 1)
    count = 0

    while wd > 0:
        count += 1
        if count % 2 == 1:
            while position.x + wd <= NUM_A:
                col = color(random(1), 1, 1, 0.3)
                fill(col)
                rect(position.x, position.y, wd, wd)
                position.x += wd
            wd = NUM_A - position.x
        else:
            while position.y + wd <= NUM_B:
                col = color(random(1), 1, 1, 0.3)
                fill(col)
                rect(position.x, position.y, wd, wd)
                position.y += wd
            wd = NUM_B - position.y
