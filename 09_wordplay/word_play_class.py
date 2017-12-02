# -*- coding: utf-8 -*-
"""
word_play_class.py
    Exercises from Think Python chapter 9
    Daniel Thomas
    October 4, 2017
"""

def print_long_words(file, n):
    ''' Exercise 9-1: prints words with more than n characters. '''
    fin = open(file)
    for line in fin:
        if len(line) > n:
            print(line)

def has_no_e(word):
    ''' Exercise 9-2: Returns True if given word does not contain the letter e'''
    for c in word:
        if c == 'e':
            return False
    return True

def avoids(word, blacklist):
    ''' Exercise 9-3: Returns True if word does not contain any characters
        in blacklist '''
    for c in word:
        if c in blacklist:
            return False
    return True

def uses_only(word, available):
    ''' Exercise 9-4: Returns True if word contains only the available characters. '''
    for c in word:
        if c not in available:
            return False
    return True

def uses_all(word, required):
    ''' Exercise 9-5: Returns True if the word uses all the required letters. '''
    return uses_only(required, word)
#    for c in letters:
#        if c not in word:
#            return False
#    return True

def is_abecedarian(word, unused=None):
    ''' Exercise 9-6: Returns True if letters in word appear in alphabetical order '''
    for i in range(len(word)-2):
        if word[i] > word[i+1]:
            return False
    return True


def check_file(file, f, arg):
    ''' Runs f(line, arg) on each line of text file. '''
    fin = open(file)
    for line in fin:
        word = line.strip()
        if f(word, arg):    #If statement using f
            print(word)

def has_e(line, unused):
    '''Returns True if the line does not contain the letter e'''
    return not has_no_e(line)

filename = 'gadsby.txt'
#fin = open(filename)
#for line in fin:
#    word = line.strip()
#    print(line)

check_file(filename, has_e, 1)

