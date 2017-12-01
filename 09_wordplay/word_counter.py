# -*- coding: utf-8 -*-
"""
word_counter.py
    Word count function for text files
    Daniel Thomas
    October 4, 2017
"""


def count_words(file):
    ''' Runs f(line, arg) on each line of text file. '''
    fin = open(file)
    n   = 0
    for line in fin:
        words = line.strip().split()
        n += len(words)
    return n

def count_characters(file):
    fin = open(file)
    n   = 0
    for line in fin:
        words = line.strip().split()
        n += sum([len(w) for w in words])
    return n


print(count_words('gadsby.txt'))
print(count_characters('gadsby.txt'))