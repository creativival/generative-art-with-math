if False:
    from lib.Processing3 import *

# fisica sample (Not work)
# Example created by Speykious


# add_library('fisica')
from fisica import Fisica, FBody, FBox, FWorld, FCircle, FDistanceJoint

world = None


def setup():
    global world
    size(400, 400)
    Fisica.init(this)
    world = FWorld()
    world.setEdges()


def draw():
    background(255)
    world.step()
    world.draw()


def mousePressed():
    b = FCircle(25)
    b.setPosition(mouseX, mouseY)
    b.setRestitution(0.5)
    b.setNoStroke()
    b.setFill(255, 80, 120)
    world.add(b)
