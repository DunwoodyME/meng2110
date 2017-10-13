# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:33:09 2017

@author: thodan
"""
import matplotlib.pyplot as plt

def plot_data(d):
    x = []
    y = []
    for key, val in d.items():
        x.append(key)
        y.append(val)
    #print(x,y)
    plt.plot(x,y,'ro')
    plt.show()

def read_data(filename):
    ''' Read a csv data file and return a dictionary containing the data '''
    fin = open(filename)
    header = fin.readline()
    data = dict()
    for line in fin:
        items = line.strip().split(',')
        data[int(items[0])] = float(items[1])
    return data

def read_data_long(filename):
    ''' Read a csv data file and return a dictionary containing the data '''
    fin = open(filename)
    header = fin.readline()
    data = dict()
    for line in fin:
        items = line.strip().split(',')
        #print(items)
        data[int(items[0])] = float(items[-1])
    return data

#print(' Motor vehicle fatalities in 2007 = {} per 100,000'\
#      .format(fatalities[2007]))
deaths = read_data_long('mvd_long.csv')
plot_data(deaths)