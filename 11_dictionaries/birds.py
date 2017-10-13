# -*- coding: utf-8 -*-
"""
birds.py
    Analyzes bird data - Homework for Think Python Chapter 11
    Daniel Thomas
    October 12, 2017
"""

def get_data(filename):
    ''' Reads the bird observations in a csv data file and calculates total count
        Returns: dictionary of birds: observances '''
    fin = open(filename)
    h   = fin.readline().strip().split(',')
    birdlist = dict()
    for line in fin:
        vals = line.strip().split(',')
        birdlist[vals[0]] = birdlist.get(vals[0],0) + int(vals[1])
    return birdlist

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val,[]).append(key)
    return inverse
    
def top_n(d, n):
    ''' Displays the birds that were sighted n or more times in the dataset '''
    print('\n  Birds reported {} or more times in 2017:'.format(n))
    for key in sorted(d):
        if d[key] >= n:
            print('    {0:23} {1:4} reported'.format(key, d[key]))
            
def add_sighting(d, birdname, number):
    ''' Add a sighting to the birdlist dictionary '''
    d[birdname] = d.get(birdname,0) + number

birds = get_data('bird_data.csv')
#print(invert_dict(birds))
add_sighting(birds, 'Wild Turkey', 6)
top_n(birds, 10)