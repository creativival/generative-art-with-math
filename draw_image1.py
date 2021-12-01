if False:
    from lib.Processing3 import *
apple, orange = None, None
apple_position = PVector(0, 0)
orange_position = PVector(0, 0)


def setup():
    global apple, orange
    size(800, 600)
    apple = loadImage("apple.png")
    orange = loadImage("orange.png")


def draw():
    background(0)
    center = PVector(width / 2, height / 2)

    apple_position.x = 250 * sin(frameCount * 0.01) + center.x
    apple_position.y = 250 * cos(frameCount * 0.01) + center.y
    orange_position.x = 200 * sin(frameCount * 0.02) + center.x
    orange_position.y = 200 * cos(frameCount * 0.02) + center.y

    image(apple, apple_position.x, apple_position.y)
    image(orange, orange_position.x, orange_position.y)
