# -*- coding: utf-8 -*-
"""
Plot_data.py
    Plot data from a file to a histogram
    Daniel Thomas
    October 11, 2017
"""

def read_data(filename):
    ''' Reads data from the given file
        filename: Name of text file containing single float per line
        returns:  List of numeric data values '''
    fin = open(filename)
    data = []
    for line in fin:
        s_list = line.strip().split(',')
        data.append([float(i) for i in s_list])
    return data

def display_data(data):
    ''' Display the grade breakdown by printing a bar chart to terminal 
        grades: List of strings for letter grades (A - F)
        returns: Nothing.  Prints the results '''
    print('\n  Motor vehicle fatalities per 100,000 population:\n')
    for year in data:
        print('   {}  {}'.format(int(year[0]), '▇'*int(year[1])))


filename = 'mvd_short.csv'
display_data(read_data(filename))