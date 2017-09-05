# -*- coding: utf-8 -*-
'''
2_fermat.py
	Ex 5-2: Checking Fermat's Last Theorem
	Daniel Thomas
	Sept 4, 2017
'''

def check_fermat(a, b, c, n):
    ''' Checks Fermat's Last Theorem:
        a^n + b^n = c^n
        '''
    lhs = a**n + b**n
    rhs = c**n
    if n > 2 and lhs == rhs:
        print('\n  %d ≠ %d' % (lhs, rhs))
        print('  Holy smokes, Fermat was wrong!')
    elif lhs == rhs:
        print('\n  %d = %d' % (lhs, rhs))
        print("  That works, but doesn't disprove Fermat")
    else: 
        print('\n  %d ≠ %d' % (lhs, rhs))
        print("  No, that doesn't work.")
    print('')

def interactive_fermat():
    ''' Prompts a user to enter values to check Fermat's Last Theorem '''
    print("\n  To check Fermat's Last Theorem, enter values for a, b, c, n")
    print("    a^n + b^n = c^n")
    a = int(input('  Enter a value for a: '))
    b = int(input('  Enter a value for b: '))
    c = int(input('  Enter a value for c: '))
    n = int(input('  Enter a value for n: '))
    check_fermat(a, b, c, n)

interactive_fermat()