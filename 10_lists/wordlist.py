# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:20:59 2017

@author: thodan
"""


filename = '../09_wordplay/words.txt'
fin = open(filename)
wordlist = []
for line in fin:
    word = line.strip()
    wordlist.append(word)

print(wordlist[-100:-1])