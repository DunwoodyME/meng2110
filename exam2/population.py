# -*- coding: utf-8 -*-
"""
population.py
    Loads population data from csv file and displays results
    Daniel Thomas
    October 19, 2017
"""

def load_data(filename):
    ''' Loads population data from csv file with given filename '''
    fin = open(filename)
    h = fin.readline()
    d = dict()
    for line in fin:
        e = line.strip().split(',')
        d[e[0]] = int(e[1]), int(e[2])
    return d

def display_density(d):
    print('\n     Country          Population density (pop/km2)')
    for country, data in d.items():
        print('  {0:30} {1:>6.1f}'.format(country, data[0]/data[1]))


data = load_data('micronesia.csv')
display_density(data)
#print(sorted(data))