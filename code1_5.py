if False:
    from lib.Processing3 import *

"""
長方形の分割によるユークリッド互除法の可視化（長方形を長方形に分割）
"""

SIZE_X = 800
SIZE_Y = 800
num_a = 10
num_b = 6
ratio = 1.0 * num_b / num_a
wd = SIZE_X * ratio
position = PVector(0, 0)


def setup():
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 1)
    div_rect()


def div_rect():
    global wd
    count = 0
    while wd > 0.1:
        count += 1
        if count % 2 == 1:
            while position.x + wd < width + 0.1:
                div_square(position, wd)
                position.x += wd
            wd = width - position.x
        else:
            while position.y + wd < width * ratio + 0.1:
                div_square(position, wd)
                position.y += wd
            wd = width * ratio - position.y


def div_square(_position, _wd):
    count = 0
    # ベクトルを作成（参照渡しにならないようにする）
    p = PVector(_position.x, _position.y)
    end_position = PVector(_wd + p.x, _wd + p.y)
    while _wd > 0.1:
        count += 1
        if count % 2 == 1:
            while p.x + _wd * ratio < end_position.x + 0.1:
                fill(color(random(1), 1, 1, 0.3))
                rect(p.x, p.y, _wd * ratio, _wd)
                p.x += _wd * ratio
            _wd = end_position.x - p.x
        else:
            while p.y + _wd / ratio < end_position.y + 0.1:
                fill(color(random(1), 1, 1, 0.3))
                rect(p.x, p.y, _wd, _wd / ratio)
                p.y += _wd / ratio
            _wd = end_position.y - p.y


def mouseClicked():
    global num_a, num_b, wd, ratio, position
    num_a = int(random(1, 20))
    num_b = int(random(1, 20))
    while num_a <= num_b:
        num_b = int(random(1, 20))
    ratio = 1.0 * num_b / num_a
    wd = SIZE_X * ratio
    position = PVector(0, 0)
    background(0, 0, 1)
    div_rect()
    print('numb_a = ' + str(num_a) + ', numb_b= ' + str(num_b))

def draw():
    pass

