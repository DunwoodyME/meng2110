# -*- coding: utf-8 -*-
"""
investment.py
    Exercise 3 from Zelle p 279:
        Determine how long many years it will take for an investment to double
    Daniel Thomas
    September 25, 2017
"""

def years_to_double(p):
    ''' Returns the number of years for an investment to double
        with an interest rate p  '''
    n = 1       # Number of years invested; start with 1
    while True:
        roi = (1 + p/100)**n  # Return on investment (amount / initial investment)
        if roi > 2.0: return n
        n += 1

rate = float(input('\n  Enter an interest rate: '))
print('  With p = %0.1f, an investment will double in %d years' % \
      (rate, years_to_double(rate)))
