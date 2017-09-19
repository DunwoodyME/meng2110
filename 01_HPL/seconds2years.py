# -*- coding: utf-8 -*-
"""
seconds2years.py
    HPL Ex 1.3: Calculates if a Norwegian baby live 1 billion seconds
    Daniel Thomas
    Aug 16, 2017
"""

seconds = 1000000000
hours   = seconds/(60*60)
days    = hours/24
years   = days/365.2422

print('\n  To live 1 billion seconds, a baby would live %g years and %g days' \
     % (int(years), int((years % 1)*365)))
if years < 82.10:
    print('  Yep, an average Norwegian baby will live 1 billion seconds.')
else:
    print('  No, a Norwegian baby will likely die before 1 billion seconds.')
    
'''
Trial run:
  To live 1 billion seconds, a baby would live 31 years and 251 days
  Yep, an average Norwegian baby will live 1 billion seconds.
'''