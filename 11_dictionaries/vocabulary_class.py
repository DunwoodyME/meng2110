# -*- coding: utf-8 -*-
"""
vocabulary_class.py
    Estimates an author's vocabulary by counting the unique words in a book
    The function is implemented using both a list and a dictionary, 
    to demonstrate the advantage of a Python dictionary in this type of problem.
    
    Requires text files from /MENG2110/class/data/
    
    Daniel Thomas
    October 16, 2017
"""

import time

def wordcount_list(filename):
    ''' Count the unique words in the given text file.
        Uses a Python list to store the set of unique words.
        Print the results '''
    fin = open(filename)
    wordlist = []   # A list for storing the unique words.
    start_time = time.process_time()  # Measure processor time for the computation
    for line in fin:
        for word in line.strip().lower().split():
            if word.isalpha():  # String method isalpha() returns True for strings with only a-z letters
                if word not in wordlist:
                    wordlist.append(word)
    print('\n  Ran wordcount_list on',filename)
    print('  Total number of words = {}'.format(len(wordlist)))
    print('  Process time = ', time.process_time()-start_time)

def wordcount_dict(filename):
    ''' Count the unique words in the given text file.
        Uses a Python dictionary to store the set of unique words, 
            and the number of occurances for each.
        Print the results '''
    fin = open(filename)
    n_words = 0     # Used to count the total number of words in the book.
    wordlist = dict()   # A dictionary for storing the unique words.
    start_time = time.process_time()
    for line in fin:
        for word in line.strip().lower().split():
            n_words += 1    # Increment total number of words, even if word is not unique.
            if word.isalpha():
                wordlist[word] = wordlist.get(word, 0) + 1
    print('\n  Ran wordcount_dict on',filename)
    print('  Total number of words = {0:,}'.format(n_words))
    print('  Number of unique words = {0:,}'.format(len(wordlist)))
    print('  Process time = ', time.process_time()-start_time)

filename = 'old_man.txt'
#filename = 'decline_and_fall.txt'  # Try this for a 1.5 million word test
wordcount_list(filename)
wordcount_dict(filename)