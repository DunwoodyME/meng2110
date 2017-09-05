# -*- coding: utf-8 -*-
'''
5_turtle_recurse.py
	Ex 5-5: Mystery turtle draw program
	Daniel Thomas
	Sept 4, 2017
'''

import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

igor = turtle.Turtle()
draw(igor, 10, 10)
turtle.done()
