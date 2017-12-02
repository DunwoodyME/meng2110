# -*- coding: utf-8 -*-
"""
triangles_class.py
    Using lists to calculate triangle area and plot triangle
    Daniel Thomas
    October 9, 2017
"""

import matplotlib.pyplot as plt

def get_vertices():
    ''' Prompt user to enter vertices of a triangle '''
    x = []
    y = []
    print('\n  Enter the vertices of a triangle: ')
    x.append(float(input('    x0: ')))
    y.append(float(input('    y0: ')))
    x.append(float(input('    x1: ')))
    y.append(float(input('    y1: ')))
    x.append(float(input('    x2: ')))
    y.append(float(input('    y2: ')))
    return [x,y]
   
def triangle_area(vertices):
    ''' Returns the area of a triangle specified by the given vertices
        Area = 1/2 |x1y2 - x2y1 - x0y2 + x2y0 + x0y1 - x1y0| '''
    x = vertices[0]
    y = vertices[1]
    a = 0.5 * abs((x[1]*y[2]-x[2]*y[1]-x[0]*y[2]+x[2]*y[0]+x[0]*y[1]-x[1]*y[0]))
    return a

def plot_triangle(vertices):
    x = vertices[0]
    y = vertices[1]
    x.append(x[0])
    y.append(y[0])
    plt.plot(x,y)
    plt.show()

#vertices = get_vertices()    # Uncomment this line to get user input
vertices = [[0,1,0],[0,0,2]]
area = triangle_area(vertices)
print('\n  The triangle area is {0}'.format(area))
plot_triangle(vertices)