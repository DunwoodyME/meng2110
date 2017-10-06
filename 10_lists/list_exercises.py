# -*- coding: utf-8 -*-
"""
list_exercises.py
    Exercises from Think Python chapter 10: Lists
    Daniel Thomas
    October 5, 2017
"""

def nested_sum(t):
    ''' Returns the sum of all integers in a nested list. '''
    total = 0
    for i in t:
        total += sum(i)
    return total

def cum_sum(t):
    ''' Returns a list with the cumulative sum of list t '''
    u = []
    for i in range(len(t)):
        u.append(sum(t[:i+1]))
    return u

def middle(t):
    ''' Returns a list of containing all but the first and last elements of t '''
    return t[1:-1]

def chop(t):
    ''' Deletes the first and last elements of a list '''
    del t[0]
    del t[-1]


t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))

t2 = [1, 2, 3]
print(cum_sum(t2))

t3 = [1, 2, 3, 4, 5, 6]
print(middle(t3))

chop(t3)
print(t3)


