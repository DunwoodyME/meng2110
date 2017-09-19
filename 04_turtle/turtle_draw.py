'''
turtle_draw.py
    Exercise from text of Chapter 4 of Think Python
    Daniel Thomas
    August 25, 2017
'''

import turtle
from math import pi, sin, radians
#from tkinter import postscript

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    angle = 360.0 / n
    polyline(t, length, n, angle)
#     for i in range(n):
#         t.fd(length)
#         t.lt(360.0/n)

def polyline(t, length, n, angle):
    ''' Draws n line segments with the given length and
    angle (in degrees) between them.  t is turtle.'''
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * pi * r
    n = int(circumference/3) + 1
    length = circumference/n
    polygon(t, length, n)

def arc(t, r, angle):
    arc_length = (2 * pi * r * angle) / 360 
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle  = float(angle) / n
    polyline(t, step_length, n, step_angle)
#    for i in range(n):
#        t.fd(length)
#        t.lt(angle/n)

def petal(t, r, angle):
    ''' Draws a petal using two arcs.
        t: Turtle
        r: radius of the arcs
        angle: angle (degrees) that subtends the arcs
    '''
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    ''' Draws a flower with n petals.
        t: Turtle
        n: number of petals
        r: radius of the arcs
        angle: angle (degrees) that subtends the arcs
    '''
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)

def circle_flower(t, r, n):
    ''' Draws a flower of radius r, composed of n circles.
        t = Turtle '''
    for i in range(n):
        circle(t,r)
        t.lt(360.0/n)

def square_flower(t, s, n):
    ''' Draws a flower composed of n squares of size s.
        t: Turtle'''
    for i in range(n):
        square(t,s)
        t.lt(360.0/n)

def spiral(t, f, size, a, n, k):
    ''' Draw a spiral using a turtle shape function f. 
        Rotates angle a and scales by k between N draw calls.
        size = size of shape (e.g. circle or square)'''
    for i in range(n):
        f(t, size)
        t.lt(a)
        size = k*size

def star(t, r, n):
    for i in range(n):
        t.fd(r)
        t.rt(180-(180/n))

bob = turtle.Turtle()
bob.speed("fastest") 
#square(bob, length = 100)
#polygon(bob, 150, 6)
circle(bob, r=50)
#arc(bob,r = 100, angle = 270)
#circle_flower(bob, 85, 20)
#flower(bob,7,100.0,60.0)
#square_flower(bob, 130, 30)

#spiral(bob, circle, 150, 10, n=100, k=0.97)
bob.hideturtle()
#ts = bob.getscreen()
#ts.getcanvas().postscript(file='spiral.eps')
turtle.done()
#turtle.exitonclick()