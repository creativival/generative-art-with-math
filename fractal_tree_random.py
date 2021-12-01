if False:
    from lib.Processing3 import *

# フラクタルツリー（非対称）
import random

tree_step = 10
tree_angle = radians(20)
tree_length = 100
tree_scale = 0.8
tree_random = 0.8
color0 = color(111, 51, 16)
color1 = color(0, 255, 0)


def setup():
    size(800, 600)
    background(255)
    translate(width / 2, height)
    branch(tree_length, tree_step)


def branch(length, n):
    # 色を変える（茶 -> 緑）
    r = map(n, tree_step, 0, red(color0), red(color1))
    g = map(n, tree_step, 0, green(color0), green(color1))
    b = map(n, tree_step, 0, blue(color0), blue(color1))
    stroke(r, g, b)
    # 線を引く
    length_to_go = length * random_range(tree_random)
    line(0, 0, 0, -length_to_go)
    translate(0, -length_to_go)
    length = length * tree_scale

    if n >= 0:
        # 左に曲がって線を引く
        pushMatrix()
        left_agree = -tree_angle * random_range(tree_random)
        rotate(left_agree)
        branch(length, n - 1)
        popMatrix()
        # 右に曲がって線を引く
        pushMatrix()
        right_agree = tree_angle * random_range(tree_random)
        rotate(right_agree)
        branch(length, n - 1)
        popMatrix()


def random_range(r):
    return random.uniform(r, 1 / r)
