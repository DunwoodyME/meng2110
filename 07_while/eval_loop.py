# -*- coding: utf-8 -*-
'''
eval.py
	Ex 7-2: Interactive eval loop
	Daniel Thomas
	Sept 23, 2017
'''

def eval_loop():
    while True:
        text = input('  Enter a Python command: ')
        if text == 'done':
            break
        print(text)
        print(eval(text))

eval_loop()