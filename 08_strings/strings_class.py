# -*- coding: utf-8 -*-
"""
strings_class.py
    In-class string exercises
    Daniel Thomas
    September 29, 2017
"""

def erase_letter(word, letter):
    ''' Prints word without the given letter '''
    edited_word = ''
    for w in word:
        if w == letter:
            edited_word += ' '
        else:
            edited_word += w
    return edited_word

print(erase_letter('Mississippi','i'))
print()
print(erase_letter('Mississippi','s'))