# -*- coding: utf-8 -*-
"""
hwk_01.py
   A simple program to compute commute time, given distance and average speed.
   Daniel Thomas
   August 14, 2017
"""
from unum.units import *

#print('This program calculates when you need to leave home to arrive at school at 7:25 a.m.')
#input1 = eval(input('Enter your distance from school in miles: '))
#input2 = eval(input('Enter your average speed in miles per hour: '))
#
#distance = input1 * mile
#speed = input2 * mile / h  
#
#time = distance / speed # Trip time in hours
#arrival = 25*min
#minutes = arrival - time.asUnit(min)
#print('  You need to leave home at 7:',minutes)

pace = 8.15 * min / mile
tempo = 7.12 * min / mile

run_duration = (1*mile * pace) + (3*mile * tempo) + (1*mile * pace)
time_after_7 = run_duration - (8*min)
print('I get home at',time_after_7,'after 7')
print('I get home at 7:',int(time_after_7.asNumber()))