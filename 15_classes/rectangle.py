# -*- coding: utf-8 -*-
"""
rectangle.py
    Contains the rectangle class from TP Chapter 15
    Daniel Thomas
    Nov 11, 2017
"""

import point
import matplotlib.pyplot as plt

class Rectangle:
    '''
    Represents a rectangle.
    Attributes: width, height, corner
    '''

def find_center(rect):
    p = point.Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def find_corners(rect):
    p1 = rect.corner
    p2, p3, p4 = point.Point(), point.Point(), point.Point()
    p2.x = p1.x + rect.width
    p2.y = p1.y
    p3.x = p2.x
    p3.y = p1.x + rect.height
    p4.x = p1.x
    p4.y = p3.y
    return p1, p2, p3, p4

def plot_line(p1, p2):
    plt.plot([p1.x,p2.x], [p1.y, p2.y])

def plot_rectangle(rect):
    c = find_corners(rect)
    for i in range(4):
        #plot_line(corners[i-1], corners[i])
        plt.plot([c[i-1].x, c[i].x], [c[i-1].y, c[i].y],'r')
    plt.show()

def plot_rectangle2(rect):
    ''' Plots the rectangle using matplotlib. '''
    corners = list(find_corners(rect))
    corners.append(corners[0])
    x = [i.x for i in corners]
    y = [i.y for i in corners]
    plt.plot(x,y)
    plt.show()

print('Printing __name__ from rectangle.py: ',__name__)
if __name__ == "__main__":
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
    center = find_center(box)
    point.print_point(center)
    plot_rectangle(box)
    grow_rectangle(box, 50, 100)
    plot_rectangle2(box)