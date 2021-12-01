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
    2,
    2,
    2,
    2,
]
speed = 10


def setup():
    size(1200, 900)
    frameRate(60)
    # フォントリストの表示
    # font_list = PFont.list()
    # for element in font_list:
    #     print(element)

    my_font = createFont(u'ＭＳ ゴシック', 30)
    textFont(my_font)

    # num = '123'
    # url = 'http://localhost:18080/kabusapi/board/{}'.format(num)
    #
    # print(url)
    #
    # s1 = '日本語文字列(s1)'
    # s2 = u'日本語文字列(s2)'
    #
    # print(s1)  # 文字化け
    # print(s2)  # 文字化けしない
    #
    # print(type(s1))  # str
    # print(type(s2))  # unicode
    #
    # print(s1.decode('utf-8'))  # str -> unicode に変換. 文字化けしない
    # print(s2.encode('utf-8'))  # unicode -> str に変換. 文字化けする
    #
    # print(s2.encode('utf-8').decode('utf-8'))  # unicode -> str -> unicode　文字化けしない


def draw():
    background(0)
    textSize(100)
    fill(100)

    # text(u'あ', 0, frameCount % 600)
    # text(u'い', 100, frameCount % 600 + 50)
    # text(u'う', 200, frameCount % 600 + 100)
    # text(u'え', 300, frameCount % 600 + 200)
    # text(u'お', 400, frameCount % 600)

    timer = 0
    for j in range(len(lyrics)):
        timer += interval_sec[j] * 60 * speed
        for i, character in enumerate(lyrics[j]):
            text(character, i * 100 + 50, (frameCount * speed - 50 * i) - timer)
