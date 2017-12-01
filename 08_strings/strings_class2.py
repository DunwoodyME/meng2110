# -*- coding: utf-8 -*-
"""
strings_class2.py
    In-class strings exercises
    Daniel Thomas
    October 2, 2017
"""

prefixes = 'JKLMNOPQ'
suffix   = 'ack'

for letter in prefixes:
    if letter == 'O':
        letter += 'u'
    elif letter == 'Q':
        letter += 'u'
    print(letter + suffix)
    #print(' (letter = {0}, suffix = {1})'.format(letter,suffix))