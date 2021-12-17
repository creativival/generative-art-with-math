if False:
    from lib.Processing3 import *
import util

"""
長方形の分割によるユークリッド互除法の可視化（正方形の再帰的な分割）
"""

SIZE_X = 500
SIZE_Y = 500
NUM_A = 10
NUM_B = 6
RATIO = 1.0 * NUM_B / NUM_A
THRESHOLD = 40


def setup():
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 1)
    div_square(PVector(0, 0), width)


def div_square(_position, _wd):
    count = 0
    # ベクトルを作成（参照渡しにならないようにする）
    p = PVector(_position.x, _position.y)
    end_position = PVector(_wd + p.x, _wd + p.y)
    fill(color(random(1), 1, 1, 0.3))
    rect(p.x, p.y, _wd, _wd)
    while _wd > THRESHOLD:
        count += 1
        if count % 2 == 1:
            while p.x + _wd * RATIO < end_position.x + 0.1:
                div_rect(p, _wd * RATIO)
                p.x += _wd * RATIO
            _wd = end_position.x - p.x
        else:
            while p.y + _wd / RATIO < end_position.y + 0.1:
                div_rect(p, _wd)
                p.y += _wd / RATIO
            _wd = end_position.y - p.y


def div_rect(_position, _wd):
    count = 0
    # ベクトルを作成（参照渡しにならないようにする）
    p = PVector(_position.x, _position.y)
    end_position = PVector(_wd + p.x, _wd / RATIO + p.y)
    fill(color(random(1), 1, 1, 0.3))
    rect(p.x, p.y, _wd, _wd / RATIO)
    while _wd > THRESHOLD:
        count += 1
        if count % 2 == 0:
            while p.x + _wd < end_position.x + 0.1:
                div_square(p, _wd)
                p.x += _wd
            _wd = end_position.x - p.x
        else:
            while p.y + _wd < end_position.y + 0.1:
                div_square(p, _wd)
                p.y += _wd
            _wd = end_position.y - p.y
