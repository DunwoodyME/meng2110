# -*- coding: utf-8 -*-
"""
right_justify.py
    Think Python Exercise 3.1
    Daniel Thomas
    August 28, 2017
"""

def right_justify(text):
    L_text = len(text)
    n_spaces = 72 - L_text
    print(n_spaces*' ',text)
    


right_justify('monty python')