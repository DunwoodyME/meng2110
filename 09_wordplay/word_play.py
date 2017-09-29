# -*- coding: utf-8 -*-
"""
word_play.py
    Exercises from Think Python chapter 9
    Daniel Thomas
    September 28, 2017
"""

def print_long_words(file, n):
    fin = open(file)
    count = 0
    for line in fin:
        if len(line) > n:
            print(line)
            count += 1
    return count

def has_no_e(word):
    for c in word:
        if c == 'e':
            return False
    return True

def print_no_e(file):
    ''' Prints words that don't contain the letter e
        Returns the percentage of words that don't have e '''
    fin = open(file)
    n_noe = 0
    n_total = 0
    for line in fin:
        n_total += 1
        if has_no_e(line):
            print(line)
            n_noe += 1
    return n_noe/n_total

def avoids(word, blacklist):
    ''' Returns true if word does not contain any blacklist characters. '''
    for c in word:
        if c in blacklist:
            return False
    return True

def uses_only(word, available):
    ''' Returns True if word contains only the available characters. '''
    for c in word:
        if c not in available:
            return False
    return True

def uses_all(word, required):
    ''' Returns True if the word uses all the required letters. '''
    return uses_only(required, word)
#    for c in letters:
#        if c not in word:
#            return False
#    return True

def is_abecedarian(w, unused):
    ''' Returns True if letters in word appear in alphabetical order '''
    for i in range(len(word)-2):
        if w[i] > w[i+1]:
            return False
    return True

def puzzler1(w, unused):
    ''' Returns True if letters in word appear in alphabetical order '''
    if len(w) >= 6:
        for i in range(len(w)-5):
            if w[i]==w[i+1] and w[i+2]==w[i+3] and w[i+4]==w[i+5]:
                return True
    return False

def is_length(w, n):
    if len(w) == n

def check_file(file, f, arg):
    ''' Runs f(line, arg) on each line of text file. '''
    fin = open(file)
    n   = 0             # Counter for number of words
    for line in fin:
        word = line.strip()
        if f(word, arg):
            print(word)
            n += 1
    return n

filename = 'words.txt'
#print(print_long_words(filename, 15))
#print('\n  {0:0.2}% of words have no e'.format(print_no_e(filename)))
#print(check_file(filename, uses_all, 'aeiouy'))
#print(is_abecedarian('abcdefa',2))
#print(check_file(filename, is_abecedarian, 'aeiouy'))
print(check_file(filename, puzzler1, 2))

