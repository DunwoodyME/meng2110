# -*- coding: utf-8 -*-
"""
power.py
    TP Exercise 6-4: Checks if one number is a power of another.
    Daniel Thomas
    September 8, 2017
"""

def is_power(a, b):
    '''Checks if number a is a power of number b '''
    #print('Entering is_power(%d,%d)' % (a,b))
#    if not (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float):
#        print('Error: Enter valid numbers for both arguments')
#        return False
    if a <= 0 or b <= 0:    # Better exception handling
        return False
    elif a == b:
        return True
    elif a % b == 0:                # If a is divisible by b...
        return is_power((a/b), b)  # check if (a/b) is a power of b
    else:
        return False

print(is_power(1024.0,2))
print(is_power(1024.0,3))

#answer = 315.1239348570238457
#print('Time required to boil from fridge = %0.1f seconds' % answer)