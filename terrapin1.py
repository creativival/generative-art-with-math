if False:
    from lib.Processing3 import *

# タートルグラフィックライブラリー
add_library('terrapin')
# from terrapin import Terrapin

def square(haba):
    for i in range(4):
        t.forward(haba)
        t.right(90)


def setup():
    global t
    size(400, 400)
    noLoop()
    colorMode(RGB, 256)
    background(0)
    strokeWeight(6)
    c1 = color(0, 0, 255)
    fill(c1)
    # create Terrapin
    t = Terrapin(this)


def draw():
    global t
    t.setLocation(50, 350)
    t.setRotation(-90)
    print(t.x, t.y, t.getRotation())
    haba = 20
    for i in range(5):
        square(haba)
        haba = haba * 2
