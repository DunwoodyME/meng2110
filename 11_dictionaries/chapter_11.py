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

print(histogram('onomatopia')) aα 
