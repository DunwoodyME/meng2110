# -*- coding: utf-8 -*-
"""
grades.py
    Calculate and display letter grades for a class.
    Daniel Thomas
    October 5, 2017
"""

import matplotlib.pyplot as plt

def read_scores(filename):
    ''' Reads scores from the given file
        filename: Name of text file containing single float per line
        returns:  List of float scores '''
    fin = open(filename)
    scores = []
    for line in fin:
        score = float(line.strip())
        scores.append(score)
    return scores

def letter_grade(score):
    ''' Converts a numeric score to a letter grade 
        score: float representing percentage out of 100
        returns: String with letter grade '''
    if 0 < score < 60: 
        return 'F'
    elif score < 70:
        return 'D'
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    elif score <= 100:
        return 'A'
    else: 
        return 'Error: score out of range'

def convert_list(scores):
    ''' Converts a list of scores to a list of grades.
        scores: list of floats representing scores out of 100.
        returns: list of strings of letter grades '''
    grades = []
    for score in scores:
        grades.append(letter_grade(score))
    return grades

def display_grades(grades):
    ''' Display the grade breakdown by printing a bar chart to terminal 
        grades: List of strings for letter grades (A - F)
        returns: Nothing.  Prints the results '''
    print('\n  Class letter grade distribution:\n')
    for letter in ['A','B','C','D','F']:
        print('   {}:  {}'.format(letter, '▇'*grades.count(letter)))

def plot_grades(grades):
    ''' Plots the grade breakdown as a matplotlib bar chart.
        grades: List of strings for letter grades (A - F)
        returns: Nothing.  Displays the bar chart '''
    letters = ['A','B','C','D','F']
    frequency = []
    for letter in letters:
        frequency.append(grades.count(letter))
    y_pos = range(len(label))
    plt.bar(y_pos, frequency)
    plt.xticks(y_pos, letters)
    plt.title('Class grade distribution') 
    plt.show()


#scores = [86.2, 91.5, 75.3, 58.2, 95.5, 62.9, 69.1, 73.2, 84.1, 89.9, 82.2]
scores = read_scores('scores.txt')
display_grades(convert_list(scores))
plot_grades(convert_list(scores))