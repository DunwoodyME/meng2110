# -*- coding: utf-8 -*-
"""
t_conversion.py
    HPL Exercise 5.12: Compare exact and inexact temperature conversion
    Daniel Thomas
    October 31, 2017
"""

import numpy as np
import matplotlib.pyplot as plt

F   = np.linspace(-20, 120, 141)
C_i = (F - 30)/2.0 
C_e = (5.0/9)*(F - 32)

#print(F)
#print(C_i)
plt.plot(F, C_i, 'r', label='Simple rule')
plt.plot(F, C_e, 'b', label='Exact conversion') # axis = [-20,-20,120,120])
plt.xlabel('Degrees Fahrenheit')
plt.ylabel('Degrees Celsius')
plt.legend()
plt.savefig('t_conversion.pdf')
plt.show()
