# -*- coding: utf-8 -*-
"""
mv_fatalities.py
    Homework 10 - writing files
    Daniel Thomas
    October 25, 2017
"""
import matplotlib.pyplot as plt

def plot_vmtpp(t):
    ''' Plot the vehicle fatality data from d using matplotlib. '''
    x = []
    y = []
    for vals in t:
        x.append(vals[0])
        y.append(vals[-1])
    plt.plot(x,y,'r.')
    plt.ylabel('Vehicle miles travelled per person')
    plt.show()

def read_data(filename):
    ''' Read a csv data file and return a dictionary containing the data '''
    fin = open(filename)
    header = fin.readline()
    data = []
    for line in fin:
        year, deaths, vmt, popn = line.strip().split(',')
        if 1924 <= int(year) < 2016:
            vmtpp = (float(vmt)*1000000000)/int(popn)
            data.append((int(year),int(deaths), float(vmt), int(popn), vmtpp))
    return data

def write_data(t, filename):
    ''' Write the data in dictionary d to a csv file '''
    try:
        fout = open(filename, 'w')
    except:
        print('ERROR: cannot open', filename)

    fout.write('Year,Deaths,VMT (billions),Population,VMT per person')
    for vals in t:
        line  = '\n'
        line += ','.join(str(i) for i in vals)
        fout.write(line)
    fout.close()

deaths = read_data('mvd_long.csv')
print(deaths)
plot_vmtpp(deaths)
write_data(deaths, 'mvd_out.csv')