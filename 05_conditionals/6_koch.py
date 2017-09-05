# -*- coding: utf-8 -*-
'''
6_koch.py
	Ex 5-6: Turtle program to draw a Koch curve.
	Daniel Thomas
	Sept 4, 2017
'''

import turtle

def koch(t, x, a):
    ''' Draws a Koch curve of length x.
        t: turtle
        a: angle, 60 for standard Koch curve '''
    if x < 3:
        t.fd(x)
    else:
        koch(t, x/3, a)
        t.lt(a)
        koch(t, x/3, a)
        t.rt(2*a)
        koch(t, x/3, a)
        t.lt(a)
        koch(t, x/3, a)

def snowflake(t, x, a):
    ''' Draws a Koch snowflake, composed of three Koch curves of length x
        t: turtle '''
    t.penup()
    t.goto(-x/2,-x/2)
    t.pendown()
    for i in range(3):
        koch(t, x, a)
        t.rt(2*a)

igor = turtle.Turtle()
#koch(igor, 200, 85)
snowflake(igor, 200, 85)
turtle.done()