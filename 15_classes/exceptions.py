# -*- coding: utf-8 -*-
"""
exceptions.py
    Demonstration of python exception handling
    Daniel Thomas
    November 8, 2017
"""
import time


try:
    while True:
        print('  Running')
        time.sleep(0.5)
except KeyboardInterrupt:
    print('\n Exiting the while loop')
finally:
    print('\n Doing some final cleanup actions')