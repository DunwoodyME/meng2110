# -*- coding: utf-8 -*-
"""
any_lowercase.py
    Exercise 8-4 from Think Python
    Daniel Thomas
    September 29, 2017
"""

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase5('substitution'))
print(any_lowercase5('haLF'))
print(any_lowercase5('ALWAYS'))