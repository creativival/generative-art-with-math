if False:
    from lib.Processing3 import *

# Not work
# Error message
# java.lang.UnsatisfiedLinkError: Can't load library: C:\Users\nspen\GitHub\processing.py\natives\windows-i586\\gluegen-rt.dll
def setup():
    size(800, 600, P3D)


def draw():
    background(0)
    translate(width / 2, height / 2)
    rotateY(PI / 6)
    box(200, 200, 200)
