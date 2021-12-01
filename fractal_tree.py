if False:
    from lib.Processing3 import *

# フラクタルツリー（対称）
tree_step = 10
tree_angle = radians(20)
tree_length = 100
tree_scale = 0.8


def setup():
    size(800, 600)
    background(255)
    translate(width / 2, height)
    branch(tree_length, tree_step)


def branch(length, n):
    # 線を引く
    line(0, 0, 0, -length)
    translate(0, -length)
    length = length * tree_scale

    if n > 0:
        # 左に曲がって線を引く
        pushMatrix()
        rotate(-tree_angle)
        branch(length, n - 1)
        popMatrix()
        # 右に曲がって線を引く
        pushMatrix()
        rotate(tree_angle)
        branch(length, n - 1)
        popMatrix()
