if False:
    from lib.Processing3 import *

# 落下する文字
lyrics = [
    u'死にたいなんて言うなよ',
    u'諦めないで生きろよ',
    u'そんな歌が正しいなんて',
    u'馬鹿げてるよな',
]
interval_sec = [
    0,
    1,
    1,
    1,
]
translate_y_speed = 0.3
DUMMY_CHARACTERS = \
    u'あいうえお' + \
    u'かきくけこ' + \
    u'さしすせそ' + \
    u'たちつてと' + \
    u'なにぬねの' + \
    u'はひふへほ' + \
    u'まみむめも' + \
    u'やゆよ' + \
    u'らりるれろ' + \
    u'わゐうゑを' + \
    u'ん' + \
    u'アイウエオ' + \
    u'カキクケコ' + \
    u'サシスセソ' + \
    u'タチツテト' + \
    u'ナニヌネノ' + \
    u'ハヒフヘホ' + \
    u'マミムメモ' + \
    u'ヤユヨ' + \
    u'ラリルレロ' + \
    u'ワヰウヱヲ' + \
    u'ン' + \
    u'ゔ' + \
    u'がぎぐげご' + \
    u'ざじずぜぞ' + \
    u'だぢづでど' + \
    u'ばびぶべぼ' + \
    u'ヴ' + \
    u'ガギグゲゴ' + \
    u'ザジズゼゾ' + \
    u'ダヂヅデド' + \
    u'バビブベボ' + \
    u'ヷヸヹヺ' + \
    u'ぱぴぷぺぽ' + \
    u'パピプペポ' + \
    u'ぁぃぅぇぉ' + \
    u'っ' + \
    u'ゃゅょ' + \
    u'ゎ' + \
    u'ァィゥェォ' + \
    u'ヵㇰヶ' + \
    u'ㇱㇲ' + \
    u'ッㇳ' + \
    u'ㇴ' + \
    u'ㇵㇶㇷㇸㇹ' + \
    u'ㇺ' + \
    u'ャュョ' + \
    u'ㇻㇼㇽㇾㇿ' + \
    u'ヮ' + \
    u'ゝ' + \
    u'ゞ' + \
    u'ヽ' + \
    u'ヾ' + \
    u'゛' + \
    u'゜' + \
    u'。' + \
    u'、'


def setup():
    size(1200, 900)
    frameRate(60)

    my_font = createFont(u'ＭＳ ゴシック', 30)
    textFont(my_font)


def draw():
    # 背景
    noStroke()
    c1 = color(238, 220, 179)
    c2 = color(100, 100, 100)
    for h in range(0, height, 5):
        r = map(h, 0, height, red(c1), red(c2))
        g = map(h, 0, height, green(c1), green(c2))
        b = map(h, 0, height, blue(c1), blue(c2))
        fill(r, g, b)
        rect(0, h, width, 5)

    pushMatrix()
    translate(0, -frameCount * translate_y_speed)

    # 文字を表示
    character_list = list(DUMMY_CHARACTERS)
    character_length = len(DUMMY_CHARACTERS)
    timer = 0
    textSize(50)
    fill(60)
    for j in range(len(lyrics)):
        timer += interval_sec[j] * 60
        for i, character in enumerate(lyrics[j]):
            timer += i * 3
            if frameCount == timer - 2 or frameCount == timer - 1:
                character_number = frameCount % character_length
                dummy_character = character_list[character_number]
                print(dummy_character)
                text(dummy_character, j * 100 + 50, j * 50 + i * 70 + 100)
            if timer <= frameCount:
                text(character, j * 100 + 50, j * 50 + i * 70 + 100)
    popMatrix()
