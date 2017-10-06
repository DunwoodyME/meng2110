# -*- coding: utf-8 -*-
"""
lists_class.py
    List Exercises in class
    Daniel Thomas
    October 6, 2017
"""

def print_elements(symbols, a_numbers):
    ''' Prints out the atomic number for each element in the symbols list'''
    for i in range(len(symbols)):
        print('  The atomic number of {0} is {1}'.format\
              (symbols[i],a_numbers[i]))
        

a = ['H','Li','Na','K', 'Rb']
n = [1, 3, 11, 19, 37]
print_elements(a,n)
#b = ['Be','Mg','Ca','Sr']
