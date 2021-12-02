if False:
    from lib.Processing3 import *

# Not work
# Error message
# Maybe there's an unclosed paren or quote mark somewhere before this line? at 0:60 in <string>
add_library("PixelFlow")


def setup():
    size(800, 600, P2D)
    global F, G
    F = DwFluid2D(DwPixelFlow(this), width, height, 1)
    G = createGraphics(width, height, P2D)


def draw():
    with G.beginDraw():
        G.background(255)
    F.addTemperature(mouseX, height - mouseY, 20, 1)
    F.update()
    F.renderFluidTextures(G, 1)
    image(G, 0, 0)
