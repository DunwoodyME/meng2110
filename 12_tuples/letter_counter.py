
'''
letter_counter.py
	Daniel Thomas
	Tests text samples to determine letter frequency.
	October 17, 2017
'''

def most_frequent(filename):
    fin = open(filename)
    letters = dict()
    for line in fin:
        for c in line.strip().lower():
            if c.isalpha():
                letters[c] = letters.get(c,0) + 1
    return letters

def display_letters(d):
    #t = []
    #for c, n in d.items():
    #    t.append((n, c))
    t = [(n,c) for c, n in d.items()]
    t.sort(reverse=True)
    for n, c in t:
        print('  {0}  {1:6,}'.format(c, n))


filename = '../11_dictionaries/old_man.txt'
histogram = most_frequent(filename)
display_letters(histogram)
