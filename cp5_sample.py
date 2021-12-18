if False:
    from lib.Processing3 import *

"""
ControlP5 sample
"""

add_library("controlP5")

SIZE_X = 500
SIZE_Y = 500
slider1 = 127


def setup():
    global cp5
    size(SIZE_X, SIZE_Y)
    cp5 = ControlP5(this)
    cp5.addSlider('slider1').setPosition(50, 100).setSize(200, 20).setRange(0, 255).setValue(127)


def draw():
    background(100)
    fill(cp5.getController('slider1').getValue())
    rect(320, 100, 20, 20)
