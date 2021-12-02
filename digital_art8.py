if False:
    from lib.Processing3 import *

# ローレンツ方程式
# https://ayumu-nagamatsu.com/archives/431/
x = 0.1
y = 0.1

# a =  0.45
# b = 1.9
# a =  1.0
# b = 0.85
# a =  1.0
# b = 0.9
a = 1.25
b = 0.75

def setup():
    size(800, 800)
    blendMode(ADD)
    background(0)
    stroke(124, 155, 255, 50)

def draw():
    global x, y
    for i in range(100):
        _x = (1 + a * b) * x - b * x * y
        _y = (1 - b) * y + b * x * x
        point(_x * 100 + width*0.5, - _y * 100 + height*0.75)
        x = _x
        y = _y