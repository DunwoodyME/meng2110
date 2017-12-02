# -*- coding: utf-8 -*-
"""
times_table_class.py
    Print out a multiplication table
    Daniel Thomas
    October 20, 2017
"""

def times_table(n):
    ''' Prints an n x n muliplication table '''
    for i in range(1,n+1): # Range can take a start and stop value
        for j in range(1,n+1):
            print('{0:3}'.format(i*j), end=' ')  
            # Read the Python docs 6.1.3 for more on the .format() method
        print()  # Print a newline character for each new row.


times_table(10)