# -*- coding: utf-8 -*-
"""
mv_fatalities.py
    Homework 10 - writing files
    Daniel Thomas
    October 25, 2017
"""
import matplotlib.pyplot as plt

def plot_vmtpp(d):
    ''' Plot the vehicle fatality data from d using matplotlib. '''
    x = []
    y = []
    for key, val in d.items():
        x.append(key)
        y.append(val[3])
    plt.plot(x,y,'r.')
    plt.ylabel('Vehicle miles travelled per person')
    plt.show()

def read_data(filename):
    ''' Read a csv data file and return a dictionary containing the data '''
    fin = open(filename)
    header = fin.readline()
    data = dict()
    for line in fin:
        year, deaths, vmt, popn = line.strip().split(',')
        if 1924 <= int(year) < 2016:
            vmtpp = (float(vmt)*1000000000)/int(popn)
            data[year] = (int(deaths), float(vmt), int(popn), vmtpp)
    return data

def write_data(d, filename):
    ''' Write the data in dictionary d to a csv file '''
    try:
        fout = open(filename, 'w')
    except:
        print('ERROR: cannot open', filename)

    fout.write('Year,Deaths,VMT (billions),Population,VMT per person')
    for key, val in d.items():
        line  = '\n'+str(key)+','
        line += ','.join(str(i) for i in val)
        fout.write(line)
    fout.close()

deaths = read_data('mvd_long.csv')
print(deaths)
plot_vmtpp(deaths)
write_data(deaths, 'mvd_out.csv')