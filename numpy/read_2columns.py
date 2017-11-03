# -*- coding: utf-8 -*-
"""
read_2columns.py
    HPL Exercise 5.14: Read and plot 2-column data
    Daniel Thomas
    Nov 2, 2017
"""

import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('xy.dat', dtype = np.float)
print(data)
x = data[:,0]
y = data[:,1]

plt.plot(x,y)
plt.title('HPL Exercise 5.14')
plt.show()