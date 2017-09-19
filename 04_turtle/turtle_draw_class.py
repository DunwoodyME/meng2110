'''
turtle_draw.py
    Turtle drawing functions from text of Chapter 4 of Think Python
    Daniel Thomas
    August 31, 2017
'''

import turtle

def square(t, length):
    ''' Draws a square with the given length
        t: turtle '''
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    ''' Draws an n-sided polygon with the given side length
        t: turtle '''
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    ''' Draws a circle of radius r
        t: turtle '''
    circumference = 2 * pi * r
    n = int(circumference/3) + 1
    length = circumference/n
    polygon(t, length, n)

def star(t, r):
    for i in range(5):
        t.fd(r)
        t.rt(36.0)

        
# Initialize your turtle and call your functions here:
bob = turtle.Turtle()
#square(bob, length = 100)
polygon(bob, 5, 100)
star(bob, 100)
#circle(bob, r=50)  # Run your other functions by calling them here.
turtle.mainloop()
