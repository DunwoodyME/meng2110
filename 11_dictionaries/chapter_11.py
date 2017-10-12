# -*- coding: utf-8 -*-
'''
chapter_11.py
	Exercises from the text of Chap 11.
	Daniel Thomas
	Oct 7, 2017
'''

def histogram(s):
    ''' From p 127-128 '''
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

def display_histogram(d):
    for letter in sorted(d):
        print(letter, '▇'*d[letter])
    
text = 'Just some random text to get us started'
display_histogram(histogram(text)) 
