if False:
    from lib.Processing3 import *

# シェルピンスキーのギャスケット
# https://ayumu-nagamatsu.com/archives/431/
MAX_LEVEL = 3  # default 5
VERT_NUM = 11  # default 3
k = 0.88  # default 0.5
alpha = 120


def setup():
    size(800, 800)
    background(0)
    blendMode(ADD)
    noFill()

    x = width / 2
    y = height / 2
    r = 200
    fractalLoop(r, x, y, 0)


def fractalLoop(_r, _x, _y, level):
    if level > MAX_LEVEL:
        return

    stroke(12 + 30 * level, 30 * level, 12 + 50 * level, alpha)
    drawShape(_r, _x, _y)

    for i in range(VERT_NUM):
        x = _r * cos(TWO_PI / VERT_NUM * (i + 0.5)) + _x
        y = _r * sin(TWO_PI / VERT_NUM * (i + 0.5)) + _y
        fractalLoop(_r * k, x, y, level + 1)


def drawShape(_r, _x, _y):
    beginShape()
    for i in range(VERT_NUM):
        x = _r * cos(TWO_PI / VERT_NUM * i) + _x
        y = _r * sin(TWO_PI / VERT_NUM * i) + _y

        vertex(x, y)

    endShape(CLOSE)
