# -*- coding: utf-8 -*-
"""
vocabulary.py
    Counts unique words in texts to assess the author's working vocabulary.
    Normal adult vocabulary 20-35,000 words
    Daniel Thomas
    October 10, 2017
"""

import time, re

def get_dictionary(filename):
    ''' Builds and returns a dictionary with keys from the wordlist '''
    fin = open(filename)
    d = {}
    for line in fin:
        d[line.strip()] = 0
    return d

def compare_dict(bookwords):
    ''' Counts the number of words from bookwords that are present in dictwords
        bookwords, dictwords: dictionaries with words as keys
        returns: number of words '''
    dictwords = get_dictionary('../09_wordplay/words.txt')
    counter = 0
    for word in bookwords:
        if word in dictwords:
            counter += 1
    return counter


def list_wordcount(filename):
    fin = open(filename)
    wordlist = []
    t0 = time.clock()
    for line in fin:
        for word in line.strip().split():
            if word not in wordlist:
                wordlist.append(word)
    cpu_time = time.clock() - t0
    #print(wordlist[0:100])
    print('\n  Executed in {0:0.6f} sec'.format(cpu_time))
    print('  Wordlist contains {} entries'.format(len(wordlist)))

def dict_wordcount(filename):
    fin = open(filename)
    wordlist = dict()
    counter = 0
    t0 = time.clock()
    for line in fin:
        for word in line.strip().lower().split():
            #if not re.search('[\W\d_]',word):
            if word.isalpha():
                counter += 1
                #word = re.sub('[\W_]+', '', word)
                wordlist[word] = wordlist.get(word,0) + 1
    cpu_time = time.clock() - t0
    print('\n  Constructed wordlist for',filename)
    print('    Execution time:      {0:9.6f}'.format(cpu_time))
    print('    Total word in text:  {0:9,}'.format(counter))
    print('    Unique words:        {0:9,}'.format(len(wordlist)))
    print('    Total crosswords:    {0:9,}'.format(compare_dict(wordlist)))
    #print('    e.g. the: {}'.format(wordlist['the']))
    #print(wordlist)



#filename = '../09_wordplay/gadsby.txt'
list_wordcount('old_man.txt')
#dict_wordcount(filename)
#dict_wordcount('hamlet.txt')
dict_wordcount('old_man.txt')
#dict_wordcount('paradise_lost.txt')
#dict_wordcount('decline_and_fall.txt')
