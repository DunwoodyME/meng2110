# -*- coding: utf-8 -*-
"""
np_arrays.py
    Introductory example of using numpy arrays
    Daniel Thomas
    Nov 1, 2017
"""

import numpy as np    # np is an alias of the imported module

def F_to_C(T_F):
    ''' Converts a temperature from Farenheit to Celsius'''
    return (5/9)*(T_F - 32.0)


T_F = [39, 32, 33, 35, 29, 27, 31]  # Given a list of temperatures in Farenheit
#T_C = [F_to_C(i) for i in T_F]     # The list comprehension way of doing it
T_F_array = np.array(T_F)           # Converting the list to an array
print(T_F_array)                    # Notice the array looks like a list
T_C = F_to_C(T_F_array)
print(T_C)
