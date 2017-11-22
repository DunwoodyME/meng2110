# -*- coding: utf-8 -*-
"""
point.py
    Contains the point class from TP Chapter 15
    Daniel Thomas
    Nov 11, 2017
"""

class Point:
    ''' Represents a point in 2-D space '''

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def distance_between_points(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return (dx**2 + dy**2)**0.5

print('Printing __name__ from point.py: ',__name__)
if __name__ == "__main__":
    a = Point()
    a.x = 3.0
    a.y = 4.0
    print_point(a)
