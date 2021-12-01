if False:
    from lib.Processing3 import *

# 回転する四角
draw_status = 0  # 1 でスタート


def setup():
    size(800, 600)
    colorMode(HSB, 100)
    frameRate(60)


def draw():
    if draw_status == 1:
        noFill()
        angle = frameCount * 0.1
        rect__width = 50 * (1 + 0.001 * frameCount)
        rect_height = 50 * (1 + 0.001 * frameCount)
        stroke(random(100), 100, 100)
        translate(mouseX, mouseY)
        rotate(angle)
        rect(0, 0, rect__width, rect_height)
    else:
        message_display()


def mousePressed():
    global draw_status
    if draw_status == 0:
        background(0)
        draw_status = 1
    else:
        draw_status = 0


def message_display():
    background(0)
    if frameCount % 60 < 40:
        textSize(20)
        fill(100)
        text('Start (Stop) to click!', 300, 260)


def random_range(r):
    return random.uniform(r, 1 / r)
