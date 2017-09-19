# -*- coding: utf-8 -*-
"""
hwk_01.py
   A simple program to compute commute time, given distance and average speed.
   Daniel Thomas
   August 14, 2017
"""

import datetime
from swampy.Lumpy import Lumpy

lumpy = Lumpy()
lumpy.make_reference()

pace = 8.15 
tempo = 7.12 
start_time = datetime.datetime(2017,8,21,hour=6,minute=52)

run_minutes = (1 * pace) + (3 * tempo) + (1 * pace)
run_duration = datetime.timedelta(minutes=run_minutes)

end_time = start_time + run_duration
print('I get home at',end_time)
lumpy.object_diagram()