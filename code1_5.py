if False:
    from lib.Processing3 import *

"""
長方形の分割によるユークリッド互除法の可視化（長方形を長方形に分割）
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


def div_square(_position, _rect_width):
    count = 0
    # ベクトルを作成（参照渡しにならないようにする）
    p = PVector(_position.x, _position.y)
    end_position = PVector(_rect_width + p.x, _rect_width + p.y)
    while _rect_width > 0.1:
        count += 1
        if count % 2 == 1:
            while p.x + _rect_width * RATIO < end_position.x + 0.1:
                fill(color(random(1), 1, 1, 0.3))
                rect(p.x, p.y, _rect_width * RATIO, _rect_width)
                p.x += _rect_width * RATIO
            _rect_width = end_position.x - p.x
        else:
            while p.y + _rect_width / RATIO < end_position.y + 0.1:
                fill(color(random(1), 1, 1, 0.3))
                rect(p.x, p.y, _rect_width, _rect_width / RATIO)
                p.y += _rect_width / RATIO
            _rect_width = end_position.y - p.y
