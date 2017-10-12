# -*- coding: utf-8 -*-
"""
material_calcs.py
    Simple deflection calculations using material properties dictionary
    Daniel Thomas
    October 12, 2017
"""

def load_materials(filename):
    ''' Reads material properties from the given file
        filename: Name of csv data file 
        returns:  Nested dictionary of properties '''
    materials = dict()
    fin = open(filename)
    h = fin.readline().strip().split(',')
    for line in fin:
        v = line.strip().split(',')
        materials[v[0]] = {h[i]:v[i] for i in [1,2,3,4]}
    return materials

def add_material(d, name, mtype, rho, E, sigma_ut):
    ''' Adds another material to the dictionary database d '''
    d[name] = {'Type':mtype, 'rho':rho, 'E':E, 'sigma_ut':sigma_ut}

def display_materials(d):
    ''' Prints out the material properties in d '''
    for m in d:
        print('{0:11} '.format(m), end='')
        for i in d[m]:
            print('{0:9}'.format(d[m][i]), end=' ')
        print()


materials = load_materials('materials.csv')
add_material(materials, 'Ti-6Al-4V', 'Titanium', 4430, 120000, 1000)
print(materials['A-36']['E'])
display_materials(materials)