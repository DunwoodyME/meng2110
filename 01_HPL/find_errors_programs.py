# -*- coding: utf-8 -*-
"""
find_errors_programs.py
    HPL Ex 1.9: Debugging textbook programs.
    Daniel Thomas
    Aug 24, 2017
"""

# a)
from math import sin, cos, pi
x = pi/4
val_1 = sin(x)**2 + cos(x)**2
print(val_1)

# b)
v0 = 3  # m/s
t  = 1  # s
a  = 2  # m/s2
s  = v0*t + 0.5*a*t**2
print(s)

# c)
a  = 3.3
b  = 5.3
a2 = a**2
b2 = b**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = (a+b)**2
eq2_pow = (a-b)**2

print('First equation:  %g = %g' % (eq1_pow, eq1_sum))
print('Second equation: %g = %g' % (eq2_pow, eq2_sum))

'''
Test run:
    1.0000000000000002
    4.0
    First equation:  73.96 = 73.96
    Second equation: 4 = 4
'''