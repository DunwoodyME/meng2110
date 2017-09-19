# -*- coding: utf-8 -*-
"""
friction_factor.py
    Homework 4, Question 2
    Daniel Thomas
    September 12, 2017
"""
from math import log10

def f_smoothpipe(Re):
    ''' Calculates the friction factor for internal flow in smooth pipes
        Re: Reynolds number, based on pipe diameter '''
    if Re < 0 or Re > 10e9:
        print('Error: Give a Reynolds number in the range 0 - 10^9')
    elif 0 < Re <= 2300:
        return 64/Re
    elif 2300 < Re <= 10e5:
        if Re < 4000: 
            print('\n  WARNING: for Re = %d, flow is in the critical zone \
                  so results many not be accurate' % Re)
        return 0.316*Re**(-1/4)
    elif 10e5 < Re < 10e9:
        return (1.8*log10(Re/6.9))**(-2)

Re1 = 3000
Re2 = 250000
print('\n  For Re = %d, f = %0.2f' % (Re1, f_smoothpipe(Re1)))
print('\n  For Re = %d, f = %0.2f' % (Re2, f_smoothpipe(Re2)))

'''
Trial Run:
  WARNING: for Re = 3000, flow is in the critical zone                   
  so results many not be accurate

  For Re = 3000, f = 0.04

  For Re = 250000, f = 0.01
'''