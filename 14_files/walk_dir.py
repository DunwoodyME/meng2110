# -*- coding: utf-8 -*-
"""
walk_dir.py
    Exercise from Think Python Chapter 14 - Files (p 168)
    Daniel Thomas
    October 24, 2017
"""

import os

def walk(dirname):
    ''' Walks a directory, printing the names of all files. '''
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

folder = '../'
walk(folder)
