if False:
    from lib.Processing3 import *

# 緑を救えゲーム
import random

# 初期値
score = 0
hp = 10
status = 1  # 0 で終了
player = {
    'x': 200,
    'y': 350,
    'width': 40,
    'height': 20
}
blocks = {
    'width': 30,
    'height': 30,
    'x_list': list(range(10)),
    'y_list': list(range(10)),
    'color_list': list(range(10)),
    'wait_list': list(range(10))
}
game = {}


def setup():
    size(400, 400)
    noStroke()
    rectMode(CENTER)
    frameRate(60)
    game_init()


def draw():
    background(0)
    if game['status']:
        game_play()
    else:
        game_over()


def player_display():
    fill(255)
    rect(player['x'], player['y'], player['width'], player['height'], 5)


def player_mode():
    player['x'] = mouseX


def block_display():
    for i in range(10):
        x = blocks['x_list'][i]
        y = blocks['y_list'][i]

        if blocks['color_list'][i] == 0:
            fill(255, 0, 0)
        else:
            fill(0, 255, 0)

        rect(x, y, blocks['width'], blocks['height'], 5)


def block_move():
    for i in range(10):
        if blocks['wait_list'][i] > 0:
            blocks['wait_list'][i] -= 1
        else:
            blocks['y_list'][i] += 2

        if blocks['y_list'][i] > height:
            if blocks['color_list'][i] == 1:
                game['hp'] -= 1
            block_init(i)


def block_init(num):
    blocks['x_list'][num] = num * 40 + 20
    blocks['y_list'][num] = 40
    blocks['color_list'][num] = random.randint(0, 1)
    blocks['wait_list'][num] = random.randint(0, 240)


def hit_check():
    for i in range(10):
        if (350 < blocks['y_list'][i] < 360) and \
                (-40 < player['x'] - blocks['x_list'][i] < 40):
            block_init(i)
            if blocks['color_list'][i] == 1:
                game['score'] += 10
            else:
                game['hp'] -= 1


def score_display():
    textSize(24)
    fill(255)
    text('score: ' + str(game['score']), 10, 25)
    text('HP: ' + str(game['hp']), 300, 25)


def game_init():
    game['score'] = score
    game['hp'] = hp
    game['status'] = status
    for i in range(10):
        block_init(i)


def game_play():
    block_move()
    block_display()
    player_mode()
    player_display()
    hit_check()
    score_display()
    if game['hp'] < 1:
        game['status'] = 0


def game_over():
    block_display()
    player_display()
    score_display()
    textSize(50)
    fill(255, 255, 0)
    text('GAME OVER', 60, 200)
    if frameCount % 60 < 40:
        textSize(20)
        fill(255)
        text('Retry to click!', 140, 260)


def mousePressed():
    if game['status'] == 0:
        game_init()
