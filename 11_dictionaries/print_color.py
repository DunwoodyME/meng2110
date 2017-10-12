# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:11:44 2017

@author: thodan
"""

from colorama import init
init()
#from termcolor import colored
#print(colored('hello', 'red'), colored('world', 'green'))
#print(colored("hello red world", 'red'))

print('\033[30m'+'Black text')
print('\033[38;2;172;34;41m'+'\033[48;2;169;173;175'+'DUNWOODY')
print('something else')  #ESC[ … 48;2;<r>;<g>;<b> … m