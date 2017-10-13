# -*- coding: utf-8 -*-
"""
build_dict.py
    Build a translation dictionary
    Daniel Thomas
    October 13, 2017
"""

def user_input(d):
    ''' Builds a dictionary by prompting the user for word, translation pairs '''
    print('\n  Enter dictionary data, first a word and then the translation')
    print('  Enter "done" to quit')
    while True:
        key = input('\n    Enter word: ')
        val = input('    Enter translation: ')
        if key == 'done' or val == 'done':
            break
        d[key] = val
    return d

def display_dict(d):
    ''' Displays the contents of dictionary d '''
    print('\n    WORD           TRANSLATION')
    for key, val in d.items():
        print('    {0:14} {1:14}'.format(key, val))


mydict = dict()
user_input(mydict)
display_dict(mydict)