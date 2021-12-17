if False:
    from lib.Processing3 import *

"""
長方形の分割によるユークリッド互除法の可視化
"""

SIZE_X = 800
SIZE_Y = 800
SCALAR = 50
NUM_A = SCALAR * 10
NUM_B = SCALAR * 6
wd = NUM_B
position = PVector(0, 0)


def setup():
    global wd
    size(SIZE_X, SIZE_Y)
    count = 0

    while wd > 0:
        count += 1
        if count % 2 == 1:
            while position.x + wd <= NUM_A:
                rect(position.x, position.y, wd, wd)
                position.x += wd
            wd = NUM_A - position.x
        else:
            while position.y + wd <= NUM_B:
                rect(position.x, position.y, wd, wd)
                position.y += wd
            wd = NUM_B - position.y


