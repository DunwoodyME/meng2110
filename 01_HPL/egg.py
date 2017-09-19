# -*- coding: utf-8 -*-
"""
egg.py
    HPL Ex 1.12: Calculates the time required to hardboil an egg.
    Daniel Thomas
    Aug 16, 2017
"""

from math import pi, log

M_s = 47.0      # [g] Mass of small egg
M_l = 67.0      # [g] Mass of large egg
rho = 1.038     # [g/cm3] Density of egg
c   = 3.7       # [J/g-K] Specific heat
K   = 0.0054    # [W/cm-K] Thermal conductivity?
T_w = 100       # [C] Water temperature
T_y = 70        # [C] Yolk temperature

# (a) Large egg from the fridge
T_o = 4         # [C] Initial temperature, from fridge
t = ((M_l**(2/3) * c * rho**(1/3)) / (K*pi**2 * (4*pi/3)**(2/3))) * \
    log(0.76 * ((T_o - T_w)/(T_y - T_w)))
minutes = int(t) // 60
seconds = int(t) % 60
print('\n  a. Time to boil large egg taken from fridge:   %g min, %g sec' \
      % (minutes, seconds) )

# (b) Large egg from room temperature
T_o = 20        # [C] Initial temperature, room temperature
t = ((M_l**(2/3) * c * rho**(1/3)) / (K*pi**2 * (4*pi/3)**(2/3))) * \
    log(0.76 * ((T_o - T_w)/(T_y - T_w)))
print('  b. Time to boil large egg at room temperature: %g min, %g sec' \
      % ((int(t) // 60), (int(t) % 60)) )

'''
Trial run:
  a. Time to boil large egg taken from fridge:   6 min, 36 sec
  b. Time to boil large egg at room temperature: 5 min, 15 sec
'''