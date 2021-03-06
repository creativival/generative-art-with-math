if False:
    from lib.Processing3 import *

"""
長方形の分割によるユークリッド互除法の可視化（正方形の再帰的な分割）
"""

add_library("controlP5")

SIZE_X = 500
SIZE_Y = 500
num_a = 10
num_b = 6
ratio = 1.0 * num_b / num_a
threshold = 40


def setup():
    size(SIZE_X, SIZE_Y)
    colorMode(HSB, 1)
    global cp5
    cp5 = ControlP5(this)
    cp5.addSlider("num_a").setPosition(20, 20).setRange(1, 40).setValue(num_a).setNumberOfTickMarks(40)
    cp5.addSlider("num_b").setPosition(20, 30).setRange(1, 40).setValue(num_b).setNumberOfTickMarks(40)
    cp5.addSlider("threshold").setPosition(20, 40).setRange(10, 400).setValue(threshold).setNumberOfTickMarks(40)
    cp5.addButton("reset_button").setLabel("RESET").setPosition(20, 160).setSize(20, 20).onClick(lambda e: reset())

    reset()


def reset():
    background(0)
    div_square(PVector(0, 0), width)


def div_square(_position, _wd):
    count = 0
    # ベクトルを作成（参照渡しにならないようにする）
    p = PVector(_position.x, _position.y)
    end_position = PVector(_wd + p.x, _wd + p.y)
    fill(color(random(1), 1, 1, 0.3))
    rect(p.x, p.y, _wd, _wd)
    while _wd > threshold:
        count += 1
        if count % 2 == 1:
            while p.x + _wd * ratio < end_position.x + 0.1:
                div_rect(p, _wd * ratio)
                p.x += _wd * ratio
            _wd = end_position.x - p.x
        else:
            while p.y + _wd / ratio < end_position.y + 0.1:
                div_rect(p, _wd)
                p.y += _wd / ratio
            _wd = end_position.y - p.y


def div_rect(_position, _wd):
    count = 0
    # ベクトルを作成（参照渡しにならないようにする）
    p = PVector(_position.x, _position.y)
    end_position = PVector(_wd + p.x, _wd / ratio + p.y)
    fill(color(random(1), 1, 1, 0.3))
    rect(p.x, p.y, _wd, _wd / ratio)
    while _wd > threshold:
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


# def mouseClicked():
#     global num_a, num_b, threshold, ratio
#     num_a = int(random(1, 20))
#     num_b = int(random(1, 20))
#     while num_a == num_b:
#         num_b = int(random(1, 20))
#     threshold = int(random(10, 200))
#     print('num_a = ' + str(num_a) + ', num_b= ' + str(num_b) + ', threshold = ' + str(threshold))
#     ratio = 1.0 * num_a / num_b
#     background(0, 0, 1)
#     div_square(PVector(0, 0), width)

def draw():
    global num_a, num_b, threshold, ratio
    num_a = int(cp5.getController('num_a').getValue())
    num_b = int(cp5.getController('num_b').getValue())
    threshold = int(cp5.getController('threshold').getValue())
    ratio = 1.0 * num_b / num_a
    print(num_a, num_b, threshold, ratio)
