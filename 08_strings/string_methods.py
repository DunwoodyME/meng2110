# -*- coding: utf-8 -*-
"""
string_methods.py
    Chapter 8 exercises from Think Python
    Daniel Thomas
    September 29, 2017
"""

def is_palindrome(word):
    if word == word[::-1]: return True

def acronym(words):
    ''' Zelle p 171, Exercise 4:
        returns an acronym for a given phrase '''
    acro = ''
    for w in words.split():
        acro += w[0].upper()
    return acro

def numerology(word):
    value = 0
    for c in word.lower():
        value += ord(c)-ord('a')+1
    return value

#print(is_palindrome('redivider'))
#print(acronym('international business machines'))
print(numerology('n'))

