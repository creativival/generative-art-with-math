if False:
    from lib.Processing3 import *

# Example created by Speykious

add_library('fisica')
# from fisica import Fisica, FBody, FBox, FWorld, FCircle, FDistanceJoint

world = None


def setup():
    global world
    size(1000, 600)
    smooth()
    frameRate(60)
    Fisica.init(this)
    world = FWorld()
    world.setGravity(0, 0)


liobj = []


def draw():
    background(50)
    global liobj
    global world

    if frameCount % 30 == 0 and frameCount < 60 ** 2:
        addObj()
        world.add(liobj[-1])
    attraction(1000)
    world.draw()
    world.step()


# The two next functions are based on the global liobj list
def addObj():
    global liobj
    obj = FCircle(random(5, 15))
    obj.setRestitution(0)
    obj.setFriction(0)
    obj.setPosition(random(100, width - 100), random(100, height - 100))
    liobj.append(obj)


def attraction(intensity):
    global liobj
    for o in liobj:
        for b in liobj:
            # An object has not to be attracted by himself
            if o != b:
                opos = PVector(o.getX(), o.getY())  # object o's position
                bpos = PVector(b.getX(), b.getY())  # object b's position

                # the two vectors's difference:
                # the vector's end is on b
                bvect = PVector.sub(bpos, opos)

                # Force created from bvect
                force = PVector.div(bvect, bvect.mag() ** 2)
                force.mult(intensity)
                # Add force to object o
                o.addForce(force.x, force.y)
