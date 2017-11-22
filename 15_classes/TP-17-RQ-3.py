# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 12:21:55 2017

@author: thodan
"""

class Time:
    """ Represents the time of day """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

start = Time(9, 45)

print_time(start)