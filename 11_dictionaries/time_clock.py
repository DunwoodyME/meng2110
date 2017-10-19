# -*- coding: utf-8 -*-
"""
time_clock.py

"""

import time

start_time = time.process_time()

#time.sleep(1.0)
for i in range(10000):
    print(i)
    
print('\n  Elapsed time = ', time.process_time() - start_time)