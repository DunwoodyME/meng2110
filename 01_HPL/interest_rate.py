# -*- coding: utf-8 -*-
"""
interest_rate.py
    HPL Ex 1.6: Calculates the growth of money in a bank.
    Daniel Thomas
    Aug 24, 2017
"""

p = 5.0     # [%] Interest rate
A = 1000    # [euros] Initial investment amount
n = 3       # [years] Number of years in bank

final_amount = A * (1 + p/100)**n
print('\n  After %d years, the € 1000 investment has grown to € %0.2f' \
      % (n,final_amount))

'''
Trial run:
  After 3 years, the € 1000 investment has grown to € 1157.63
'''