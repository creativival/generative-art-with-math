#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ユークリッド互除法

a = 14803
b = 12707
quotient = 0
remainder = b
count = 0

while remainder > 0:
    print(a, b)
    count += 1
    quotient = a // b  # 切り捨て除算
    remainder = a % b
    a = b
    b = remainder

print(u'試行回数' + str(count))
print(u'最大公約数は' + str(a))


