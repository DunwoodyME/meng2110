# -*- coding: utf-8 -*-
'''
3_triangle.py
	Ex 5-3: Checks if 3 sticks could form a triangle
	Daniel Thomas
	Sept 4, 2017
'''

def is_triangle(a, b, c):
    ''' Takes three stick lengths and checks if they could form a triangle.'''
    if   a >= (b+c): print('No')
    elif b >= (a+c): print('No')
    elif c >= (a+b): print('No')
    else:           print('Yes')

def check_triangle():
    ''' Prompts user to input 3 stick length, and checks if they could form a triangle'''
    print('\n  Enter three stick lengths, and check if they will make a triangle')
    a = int(input('    First stick: '))
    b = int(input('    Second stick:'))
    c = int(input('    Third stick: '))
    #print('  Result: ', end=' ')
    is_triangle(a,b,c)

check_triangle()