if False:
    from lib.Processing3 import *

"""
長方形の分割によるユークリッド互除法の可視化（再帰）
"""

SIZE_X = 800
SIZE_Y = 800
NUM_A = 10
NUM_B = 7
RATIO = 1.0 * NUM_B / NUM_A
rect_width = SIZE_X * RATIO
position = PVector(0, 0)


def setup():
    global rect_width
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 1)
    count = 0

    while rect_width > 0.1:
        count += 1
        if count % 2 == 1:
            while position.x + rect_width < width + 0.1:
                div_square(position, rect_width)
                position.x += rect_width
            rect_width = width - position.x
        else:
            while position.y + rect_width < width * RATIO + 0.1:
                div_square(position, rect_width)
                position.y += rect_width
            rect_width = width * RATIO - position.y
            print(rect_width)


def div_square(_position, _rect_width):
    count = 0
    position_x = _position.x
    position_y = _position.y
    end_position = PVector(_rect_width + position_x, _rect_width + position_y)
    # print(end_position)
    while _rect_width > 0.1:
        count += 1
        # print(count)
        if count % 2 == 1:
            while position_x + _rect_width * RATIO < end_position.x + 0.1:
                fill(color(random(1), 1, 1, 0.3))
                rect(position_x, position_y, _rect_width * RATIO, _rect_width)
                position_x += _rect_width * RATIO
            _rect_width = end_position.x - position_x
            # print(_rect_width)
        else:
            while position_y + _rect_width / RATIO < end_position.y + 0.1:
                fill(color(random(1), 1, 1, 0.3))
                rect(position_x, position_y, _rect_width, _rect_width / RATIO)
                position_y += _rect_width / RATIO
            _rect_width = end_position.y - position_y
            # print(_rect_width)