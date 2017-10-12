# -*- coding: utf-8 -*-
"""
histogram.py
    Use a dictionary as a counter to build a histogram
    Daniel Thomas
    October 11, 2017
"""

def histogram(s):
    ''' Counts the number of occurances of each character in a string
        Returns: dictionary containing letter: frequency items '''
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def display_histogram(d):
    ''' Displays the histogram contained in dictionary d '''
    for key in d:
        print(key,d[key]*'▇')

text = 'sippity sip on the mississippi'
text_dict = histogram(text)
display_histogram(text_dict)
