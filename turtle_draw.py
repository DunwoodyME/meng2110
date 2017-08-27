'''
turtle_draw.py
    Exercise from text of Chapter 4 of Think Python
    Daniel Thomas
    August 25, 2017
'''

import turtle
from math import pi, sin, radians

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
    print(length,n)
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
    
def flower(t, r, n):
    ''' Draws the turtle flowers of Ex 4.2, with n petals.'''
    petal_angle = 360.0 / n
    arc_angle   = petal_angle
    arc_radius  = r / (2*sin(radians(arc_angle)/2))
    print(arc_angle, arc_radius)
    for i in range(n):
        arc(t, arc_radius, arc_angle)
        t.lt(petal_angle)
        arc(t, arc_radius, arc_angle)
        t.lt(180)


bob = turtle.Turtle()
#square(bob, length = 100)
#polygon(bob, 150, 6)
#circle(bob, r=50)
#arc(bob,r = 100, angle = 270)
flower(bob, 80, 5)
print(bob)
turtle.mainloop()