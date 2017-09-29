# -*- coding: utf-8 -*-
"""
caesar_cypher.py
    Exercise 8-5 from Think Python
    Daniel Thomas
    September 29, 2017
"""

def rotate_word(word, n):
    ''' Rotates a word by the n characters.'''
    rword = ''
    for c in word.lower():
        i = ord(c) + n
        if i > ord('z'):
            i = ord('a') - 1 + (i - ord('z'))
        elif i < ord('a'):
            i = ord('z') + 1 - (ord('a') - i)
        rword += chr(i)
    return rword

print(rotate_word('zabcd',3))        