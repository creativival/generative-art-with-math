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
rect_width = NUM_B
position = PVector(0, 0)
iteration = 0


def setup():
    global rect_width, iteration
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 1)

    while rect_width > 0:
        iteration += 1
        if iteration % 2 == 1:
            while position.x + rect_width <= NUM_A:
                col = color(random(1), 1, 1, 0.3)
                fill(col)
                rect(position.x, position.y, rect_width, rect_width)
                position.x += rect_width
            rect_width = NUM_A - position.x
        else:
            while position.y + rect_width <= NUM_B:
                col = color(random(1), 1, 1, 0.3)
                fill(col)
                rect(position.x, position.y, rect_width, rect_width)
                position.y += rect_width
            rect_width = NUM_B - position.y
