# -*- coding: utf-8 -*-
"""
mvd_class.py
    Plot data from the motor vehicle deaths dataset
    Daniel Thomas
    October 20, 2017
"""

import matplotlib.pyplot as plt

def plot_data(d):
    ''' Plot deaths/VMT vs year, for the data in the dictionary d '''
    x = []  # First job is to create lists of x,y values for plt.plot()
    y = []
    for key, val in d.items():
        x.append(key)           # the keys in d are the years
        y.append(val[0]/val[1]) # this is: VMT/population
    plt.plot(x,y,'r.')
    plt.ylabel('deaths/bill vehicle mile traveled')  # Add a y-axis label
    plt.show()                  # Required to display the plot

def read_data(filename):
    ''' Read a csv data file and return a dictionary containing the data '''
    fin = open(filename)
    header = fin.readline()
    data = dict()   # Use a dictionary container for the data
    for line in fin:
        # Below: using tuple assignment for data values from year row 
        year, deaths, vmt, popn = line.strip().split(',')
        if 1925 <= int(year) < 2016:    # Ignore years with no VMT data
            data[int(year)] = (int(deaths), float(vmt))
    return data

d = read_data('mvd_long.csv')
plot_data(d)