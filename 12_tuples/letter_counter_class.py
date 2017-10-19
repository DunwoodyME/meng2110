# -*- coding: utf-8 -*-
"""
letter_counter_class.py
    Count the frequency of letter use in a text
    Daniel Thomas
    October 18, 2017
"""

def histogram(s):
    ''' Returns a dictionary mapping each character in string s
        to the frequency of occurance. '''
    d = dict()
    for c in s.lower():
        d[c] = d.get(c, 0) + 1
    return d
    
def display_freq(d):
    ''' Prints the histogram data in dictionary d '''
    t = []
    for key, value in d.items():
        # append each (freq, letter) pair as a tuple
        t.append((value,key))
    t.sort(reverse=True)
    for pair in t:
        print(pair[1], pair[0])

text = 'Some sample text with multiple letters'
d = histogram(text)
display_freq(d)
