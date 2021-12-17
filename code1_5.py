if False:
    from lib.Processing3 import *
import util

"""
長方形の分割によるユークリッド互除法の可視化（長方形を長方形に分割）
"""

SIZE_X = 800
SIZE_Y = 800
NUM_A = 10
NUM_B = 7
RATIO = 1.0 * NUM_B / NUM_A
wd = SIZE_X * RATIO
position = PVector(0, 0)


def setup():
    global wd
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 1)
    count = 0

    while wd > 0.1:
        count += 1
        if count % 2 == 1:
            while position.x + wd < width + 0.1:
                util.div_square(position, wd, RATIO)
                position.x += wd
            wd = width - position.x
        else:
            while position.y + wd < width * RATIO + 0.1:
                util.div_square(position, wd, RATIO)
                position.y += wd
            wd = width * RATIO - position.y


# def div_square(_position, _wd):
#     count = 0
#     # ベクトルを作成（参照渡しにならないようにする）
#     p = PVector(_position.x, _position.y)
#     end_position = PVector(_wd + p.x, _wd + p.y)
#     while _wd > 0.1:
#         count += 1
#         if count % 2 == 1:
#             while p.x + _wd * RATIO < end_position.x + 0.1:
#                 fill(color(random(1), 1, 1, 0.3))
#                 rect(p.x, p.y, _wd * RATIO, _wd)
#                 p.x += _wd * RATIO
#             _wd = end_position.x - p.x
#         else:
#             while p.y + _wd / RATIO < end_position.y + 0.1:
#                 fill(color(random(1), 1, 1, 0.3))
#                 rect(p.x, p.y, _wd, _wd / RATIO)
#                 p.y += _wd / RATIO
#             _wd = end_position.y - p.y
