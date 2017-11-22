# -*- coding: utf-8 -*-
"""
simple_time.py
    Time class definition from Think Python Chapter 16
    Daniel Thomas
    November 13, 2017
"""

class Time:
    ''' Represents the time of day 
        Attributes: hour, minute, second
    '''

def print_time(t):
    ''' Print out a Time object in the format HH:MM:SS '''
    print('%.2d:%.2d:%.2d' %(t.hour,t.minute,t.second))

def time_to_int(time):
    ''' Converts a Time object to an integer for number of seconds '''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    ''' Converts a number of seconds to a Time object '''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    ''' Returns the sum of two Time objects '''
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def increment(time, seconds):
    ''' Modifies a Time object, incrementing the value by given number of seconds '''
    return int_to_time(time_to_int(time) + seconds)

def is_after(t1, t2):
    ''' Returns True if t1 follows t2 chronologically; 
        Returns False otherwise '''
# Version 1:
#    if (t1.hour*3600 + t1.minute*60 + t1.second) > \
#        (t2.hour*3600 + t2.minute*60 + t2.second):
#            return True
#    else:   return False
# Version 2:
#    return (t1.hour*3600 + t1.minute*60 + t1.second) > \
#        (t2.hour*3600 + t2.minute*60 + t2.second)
# Version 3:
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second) 

if __name__ == '__main__':
    t = Time()
    t.hour = 8
    t.minute = 14
    t.second = 30

    t2 = Time()
    t2.hour = 9
    t2.minute = 14
    t2.second = 30

    print(time_to_int(int_to_time(360)))
    print_time(int_to_time(time_to_int(t)))
    print_time(increment(t2, 50))