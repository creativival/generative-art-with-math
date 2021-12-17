#!/usr/bin/python
# -*- coding: utf-8 -*-

if False:
    from lib.Processing3 import *

def div_square(_position, _wd, RATIO):
    count = 0
    # ベクトルを再生成（参照渡しにならないため）
    p = PVector(_position.x, _position.y)
    end_position = PVector(_wd + p.x, _wd + p.y)
    while _wd > 0.1:
        count += 1
        if count % 2 == 1:
            while p.x + _wd * RATIO < end_position.x + 0.1:
                fill(color(random(1), 1, 1, 0.3))
                rect(p.x, p.y, _wd * RATIO, _wd)
                p.x += _wd * RATIO
            _wd = end_position.x - p.x
        else:
            while p.y + _wd / RATIO < end_position.y + 0.1:
                fill(color(random(1), 1, 1, 0.3))
                rect(p.x, p.y, _wd, _wd / RATIO)
                p.y += _wd / RATIO
            _wd = end_position.y - p.y
