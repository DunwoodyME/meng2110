# -*- coding: utf-8 -*-
"""
sed_class.py
    Think Python Exercise 14-1: Replacing a pattern string in a text file
    Daniel Thomas
    October 25, 2017
"""

def sed(search, replace, infile, outfile):
    '''
    Replaces a string from a text file and writes to a new file
        search:  String pattern to search for in file
        replace: Replacement string
        infile:  Filename of file to search
        outfile: Filename of new output file
    '''
    fin  = open(infile, 'r')
    fout = open(outfile, 'w')
    
    for line in fin:
        line = line.replace(search, replace)
        fout.write(line)
    
    fin.close()
    fout.close()

# To run these examples you should copy the hamlet_to_be.txt file from /class/data/
sed('fardels','burdens','hamlet_to_be.txt','hamlet_edited.txt')
sed('â€™',"'",'hamlet_to_be.txt','hamlet_edited.txt')        
        
        
        
        







