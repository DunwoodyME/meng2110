# -*- coding: utf-8 -*-
"""
sed.py
    Exercise 14-1 from Think Python
    Daniel Thomas
    October 24, 2017
"""

def sed(pattern, replacement, infile, outfile):
    try:
        fin = open(infile, 'r')
    except:
        print('ERROR: could not open',infile)
    fout = open(outfile, 'w')
    
    for line in fin:
        line = line.replace(pattern, replacement)
        fout.write(line)
    
    fin.close()
    fout.close()

def main():
    sed('fardels', 'burdens', 'hamlet_to_be.txt', 'hamlet_edited.txt')

if __name__ == '__main__':
    main()