# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:05:09 2017

@author: thodan
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.1)
y = np.sin(x)

plt.plot(x,y, label='sin(x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0,2*np.pi)
plt.legend()
plt.show()