if False:
    from lib.Processing3 import *

# シェルピンスキーのギャスケット（線画）
num = 0


def setup():
    size(550, 550)
    frameRate(60)
    noStroke()
    background(255)


def draw():
    # 基本の三角形を描画
    x = width / 2
    y = 20
    edge = 500
    background(255)
    fill(0)
    triangle(
        x,
        y,
        x + edge * sin(PI / 6),
        y + edge * cos(PI / 6),
        x - edge * sin(PI / 6),
        y + edge * cos(PI / 6)
    )
    # 内側の三角形を描画
    display_triangle(
        x,
        y,
        x + edge * sin(PI / 6),
        y + edge * cos(PI / 6),
        x - edge * sin(PI / 6),
        y + edge * cos(PI / 6),
        num
    )
    # n を表示
    textSize(20)
    fill(0)
    text('n = ' + str(num), 300, 30)

    # 初期画面でメッセージを表示
    if num == 0:
        display_message()


def display_message():
    if frameCount % 60 < 40:
        textSize(20)
        fill(0)
        text('Click triangle!', 10, 30)


def display_triangle(x1, y1, x2, y2, x3, y3, n):
    if 0 < n:
        new_x1 = (x2 + x3) / 2
        new_y1 = (y2 + y3) / 2
        new_x2 = (x3 + x1) / 2
        new_y2 = (y3 + y1) / 2
        new_y3 = (y1 + y2) / 2
        new_x3 = (x1 + x2) / 2

        noFill()
        stroke(255)
        strokeWeight(1)
        triangle(
            new_x1,
            new_y1,
            new_x2,
            new_y2,
            new_x3,
            new_y3,
        )

    if 1 < n:
        display_triangle(x1, y1, new_x2, new_y2, new_x3, new_y3, n - 1)
        display_triangle(new_x1, new_y1, x2, y2, new_x3, new_y3, n - 1)
        display_triangle(new_x1, new_y1, new_x2, new_y2, x3, y3, n - 1)


def mousePressed():
    global num
    if mouseButton == LEFT:
        num += 1
    elif mouseButton == RIGHT:
        num = max(num - 1, 0)
    redraw()
