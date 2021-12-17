#!/usr/bin/python
# -*- coding: utf-8 -*-

if False:
    from lib.Processing3 import *

def div_square(_position, _rect_width, RATIO):
    count = 0
    # ベクトルを再生成（参照渡しにならないため）
    p = PVector(_position.x, _position.y)
    end_position = PVector(_rect_width + p.x, _rect_width + p.y)
    while _rect_width > 0.1:
        count += 1
        if count % 2 == 1:
            while p.x + _rect_width * RATIO < end_position.x + 0.1:
                fill(color(random(1), 1, 1, 0.3))
                rect(p.x, p.y, _rect_width * RATIO, _rect_width)
                p.x += _rect_width * RATIO
            _rect_width = end_position.x - p.x
        else:
            while p.y + _rect_width / RATIO < end_position.y + 0.1:
                fill(color(random(1), 1, 1, 0.3))
                rect(p.x, p.y, _rect_width, _rect_width / RATIO)
                p.y += _rect_width / RATIO
            _rect_width = end_position.y - p.y
