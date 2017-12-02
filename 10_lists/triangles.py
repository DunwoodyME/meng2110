# -*- coding: utf-8 -*-
"""
triangles.py
    Compute triangle area and plot the triangle
    Daniel Thomas
    October 9, 2017
"""

import matplotlib.pyplot as plt

def get_triangle():
    ''' Prompts user to enter vertices for a triangle 
        returns: Nested list of three vertices. '''
    print('\n  Enter the coordinates of three vertices of a triangle.')
    v1 = [float(i) for i in input('    x1, y1:  ').split(',')]
    v2 = [float(i) for i in input('    x2, y2:  ').split(',')]
    v3 = [float(i) for i in input('    x3, y3:  ').split(',')]
    return [v1, v2, v3]
    

def triangle_area(vertices):
    xy = list(zip(*vertices))
    x = list(xy[0])
    y = list(xy[1])
    # do x.insert(0,10) so that index matches equation?
    area = 0.5*abs(x[1]*y[2] - x[2]*y[1] - x[0]*y[2] + x[2]*y[0] + x[0]*y[1] - x[1]*y[0])
    print(area)
    
def plot_triangle(vertices):
    xy = list(zip(*vertices))
    x = list(xy[0])
    y = list(xy[1])
    x.append(x[0])
    y.append(y[0])
    plt.plot(x,y)
    plt.show()

test = [[0,0], [1,0], [0,2]]
triangle_area(test)
plot_triangle(test)
#print(get_triangle())