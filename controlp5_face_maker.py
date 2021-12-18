if False:
    from lib.Processing3 import *

"""
ControlP5 sample
https://tabreturn.github.io/code/processing/python/2019/03/19/processing.py_in_ten_lessons-7.5-_controlp5.html
"""

add_library('controlP5')


def setup():
    size(720, 485)
    global cp5
    cp5 = ControlP5(this)
    (cp5.addTextfield('alias')
     .setPosition(500, 20)
     .setSize(200, 25)
     )
    (cp5.addSlider('eye distance')
     .setPosition(500, 80)
     .setSize(200, 20)
     .setRange(30, 120)
     .setValue(80)
     )
    (cp5.getController('eye distance')
     .getCaptionLabel()
     .align(ControlP5.LEFT, ControlP5.BOTTOM_OUTSIDE)
     .setPaddingX(0)
     )
    (cp5.addKnob('eye size')
     .setPosition(515, 135)
     .setRadius(35)
     .setRange(10, 60)
     .setValue(50)
     )

    (cp5.addToggle('heavy brow')
     .setPosition(635, 138)
     .setSize(20, 20)
     )

    (cp5.addToggle('sleepless')
     .setPosition(635, 185)
     .setSize(20, 20)
     )
    (cp5.addSlider2D('nose position')
     .setPosition(500, 240)
     .setSize(200, 100)
     .setMinMax(-30, -20, 30, 20)
     .setValue(0, 0)
     )
    (cp5.addSlider('mouth width')
     .setPosition(500, 375)
     .setSize(200, 20)
     .setRange(10, 200)
     .setValue(124)
     .setNumberOfTickMarks(6)
     .setSliderMode(Slider.FLEXIBLE)
     )
    (cp5.getController('mouth width')
     .getCaptionLabel()
     .align(ControlP5.LEFT, ControlP5.BOTTOM_OUTSIDE)
     .setPaddingX(0)
     .setPaddingY(12)
     )
    (cp5.addButton('save image')
     .setPosition(500, 440)
     .setSize(200, 25)
     # .onClick(lambda e: println(e.getController().getInfo()))  # コンソールに出力
     .onClick(lambda e: save(cp5.getController('alias').getText()))  # 画像を保存
     )


def draw():
    background('#004477')
    stroke('#FFFFFF')
    strokeWeight(3)
    axis = 250

    # face
    noFill()
    ellipse(axis, 220, 370, 370)
    # alias
    fill('#FFFFFF')
    textSize(20)
    textAlign(CENTER)
    alias = cp5.getController('alias').getText()
    text(alias, axis, 450)
    noFill()
    # eyes
    eyedistance = cp5.getController('eye distance').getValue()
    eyesize = cp5.getController('eye size').getValue()
    ellipse(axis - eyedistance, 180, eyesize, eyesize)
    ellipse(axis + eyedistance, 180, eyesize, eyesize)

    if cp5.getController('heavy brow').getValue():
        fill('#004477');
        stroke('#004477')
        rect(100, 180 - eyesize / 2, 300, eyesize / 2)
        stroke('#FFFFFF')
        line(
            axis - eyedistance - eyesize / 2 - 5, 180,
            axis + eyedistance + eyesize / 2 + 5, 180
        )

    if cp5.getController('sleepless').getValue():
        noFill()
        arc(axis - eyedistance, 190, eyesize, eyesize, 0, HALF_PI)
        arc(axis + eyedistance, 190, eyesize, eyesize, HALF_PI, 2.5)
        fill('#004477')

    # nose
    noseposition = cp5.getController('nose position')
    nosex = noseposition.getArrayValue()[0]
    nosey = noseposition.getArrayValue()[1]
    line(axis - 10 + nosex, 180 + nosey, axis - 10 + nosex, 300 + nosey)
    line(axis - 10 + nosex, 300 + nosey, axis - 10 + nosex + 30, 300 + nosey)

    # mouth
    mouthwidth = cp5.getController('mouth width').getValue()
    line(axis - mouthwidth / 2, 340, axis + mouthwidth / 2, 340)
