if False:
    from lib.Processing3 import *

"""
長方形の分割によるユークリッド互除法の可視化（正方形に変形）
"""

SIZE_X = 800
SIZE_Y = 800
NUM_A = 16
NUM_B = 7
RATIO = 1.0 * NUM_B / NUM_A
rect_width = SIZE_X
position = PVector(0, 0)


def setup():
    global rect_width
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 1)
    count = 0

    while rect_width > 0:
        count += 1
        if count % 2 == 1:
            while position.x + rect_width * RATIO < width + 0.1:
                col = color(random(1), 1, 1, 0.3)
                fill(col)
                rect(position.x, position.y, rect_width * RATIO, rect_width)
                position.x += rect_width * RATIO
            rect_width = width - position.x
        else:
            while position.y + rect_width / RATIO < width + 0.1:
                col = color(random(1), 1, 1, 0.3)
                fill(col)
                rect(position.x, position.y, rect_width, rect_width / RATIO)
                position.y += rect_width / RATIO
            rect_width = width - position.y
