# -*- coding: utf-8 -*-
"""
gcd.py
    Think Python Exercise 6-5
    Daniel Thomas
    September 12, 2017
"""

import math

def gcd(a,b):
    x = max(a,b)
    y = min(a,b)
    r = x % y
    print('  gcd(%d,%d)' % (a,b))
    if r == 0:
        return y
    elif y == 0:
        return x
    else:
        return gcd(y,r)

a = 56
b = 476
print('\n  gcd(%d,%d) = %d' % (a,b,gcd(a,b)))
print('  math.gcd() = %d' % math.gcd(a,b))

'''
Test run:

'''