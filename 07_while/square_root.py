# -*- coding: utf-8 -*-
'''
square_root.py
	Ex 7-1: Square root estimate.
	Daniel Thomas
	Sept 23, 2017
'''

import math

def mysqrt(a):
    x = a/2.0
    delta = 0.1
    while delta > 0.00000001:
        y = (x + a/x) / 2
        delta = abs(y - x)
        x = y
    return x

def test_square_root():
    print('   a   mysqrt(a)  math.sqrt(a)  diff')
    print('  ---  ---------  ------------  ----')
    for a in range(1,10):
        diff = abs(math.sqrt(a) - mysqrt(a))
        print('  %0.1f  %0.7f  %0.9f   %g' %(a, mysqrt(a), math.sqrt(a), diff))

test_square_root()