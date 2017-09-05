# -*- coding: utf-8 -*-
'''
4_recurse.py
	Ex 5-4: Simple recurvise function
	Daniel Thomas
	Sept 4, 2017
'''

def recurse(n, s):
    ''' Recurse sums all the integers from 0 to n, adds the total to s and prints s.'''
    if n == 0:
        print(s)
    else:
        print('n=%d, s=%d' % (n,s))
        recurse(n-1, n+s)

recurse(4,0)