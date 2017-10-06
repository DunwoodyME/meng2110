# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:48:17 2017

@author: thodan
"""

import matplotlib.pyplot as plt

label = ('A','B','C','D','F')
y_pos = range(len(label))
value = (12,29,20,13,5)
plt.bar(y_pos, value)
plt.xticks(y_pos, label)
plt.title('Class grade distribution')
plt.show()
