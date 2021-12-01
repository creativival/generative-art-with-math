if False:
    from lib.Processing3 import *

# 振動する円
draw_status = 0  # 1 でスタート
figure = {}


def setup():
    size(800, 600)
    # colorMode(HSB, 100)
    frameRate(60)
    background(255)
    figure['x'] = 300
    figure['y'] = 200


def draw():
    if draw_status == 1:
        fill(0, 5)
        noStroke()
        rect(0, 0, 800, 600)
        stroke(random(255), random(255), 255)
        strokeWeight(4)
        noFill()
        ellipse(figure['x'], figure['y'], 180, 180)
        figure['x'] += random(-4, 4)
        figure['y'] += random(-4, 4)
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
