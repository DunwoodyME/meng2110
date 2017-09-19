# -*- coding: utf-8 -*-
"""
one_liter.py
    HPL Ex 1.5: Calculates the mass of various substances.
    Daniel Thomas
    Aug 24, 2017
"""

# Material densities from textbook, in g/cc or kg/L
rho_iron = 7.8
rho_air = 0.0012
rho_gasoline = 0.67
rho_ice = 0.9
rho_human_body = 1.03
rho_silver = 10.5
rho_platinum = 21.4

v = 1.0 # [L] Volume for calculation
print('\n  The mass of 1 liter of various substances is given below:')
print('  - Iron:     %6.3f kg' % (v*rho_iron))
print('  - Air:      %6.3f kg' % (v*rho_air))
print('  - Gasoline: %6.3f kg' % (v*rho_gasoline))
print('  - Ice:      %6.3f kg' % (v*rho_ice))
print('  - Human:    %6.3f kg' % (v*rho_human_body))
print('  - Silver:   %6.3f kg' % (v*rho_silver))
print('  - Platinum: %6.3f kg' % (v*rho_platinum))

'''
Test run:
  The mass of 1 liter of various substances is given below:
  - Iron:      7.800 kg
  - Air:       0.001 kg
  - Gasoline:  0.670 kg
  - Ice:       0.900 kg
  - Human:     1.030 kg
  - Silver:   10.500 kg
  - Platinum: 21.400 kg
'''