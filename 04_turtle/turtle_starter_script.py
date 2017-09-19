'''
turtle_draw.py
    Turtle drawing functions from text of Chapter 4 of Think Python
    Daniel Thomas
    August 31, 2017
'''

import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def circle(t, r):
    circumference = 2 * pi * r
    n = int(circumference/3) + 1
    length = circumference/n
    polygon(t, length, n)

def star(t, r):
    for i in range(5):
        t.fd(r)
        t.rt(36.0)

# Your other function definitions go here.
# e.g. def circle(t,r): ...
        
# Initialize your turtle and call your functions here:
bob = turtle.Turtle()
square(bob, length = 100)
#star(bob, 100)
#circle(bob, r=50)  # Run your other functions by calling them here.
turtle.mainloop()
