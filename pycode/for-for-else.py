#!/usr/bin/python
# -*- coding: UTF-8 -*-
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print '%d 等于 %d * %d' % (num, i, j)
            break
    else:
        print num, '是一个质数'
