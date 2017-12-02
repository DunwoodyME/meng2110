# -*- coding: utf-8 -*-
"""
countries.py
    Practical Programming Exercise 14.8.1 (p293)
    Implement Country and Continent classes
    Daniel Thomas
    Nov 8, 2017
"""

class Country:
    ''' Represents a country '''

class Continent:
    ''' Represents a continent '''
    

def larger_area(a, b):
    if a.area > b.area:
        return a
    elif a.area < b.area:
        return b
    else:
        print('The areas are equal')
        return None

def print_country(a):
    print('\n  {}:'.format(a.name))
    print('  - Population:   {0:,}'.format(a.population))
    print('  - Area:         {0:,} km2'.format(a.area))
    print('  - Pop. density: {0:0.2f} people/km2'.format(population_density(a)))

def print_continent(c):
    print('\n{}:'.format(c.name))
    for country in c.countries:
        print_country(country)

def population_density(c):
    return c.population/c.area

if __name__ == '__main__':

    usa = Country()
    usa.name = 'United States of America'
    usa.population = 313914040
    usa.area = 9826675

    canada = Country()
    canada.name = 'Canada'
    canada.population = 34482779
    canada.area = 9984670

    mexico = Country()
    mexico.name = 'Mexico'
    mexico.population = 127540423
    mexico.area = 1964375

    n_america = Continent()
    n_america.name = 'North America'
    n_america.countries = [canada, usa, mexico]
    
    print_continent(n_america)
    #print(larger_area(usa, canada).name)    
    #print('\n The population density of {0} is {1:0.1f}'.format(
    #        usa.name, population_density(usa)))