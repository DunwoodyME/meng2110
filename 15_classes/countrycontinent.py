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
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
    
    def __str__(self):
        output  = '\n  {0}:'.format(self.name)
        output += '\n  - Population:   {0:,}'.format(self.population)
        output += '\n  - Area:         {0:,} km²'.format(self.area)
        output += '\n  - Pop. Density: {0:0.2f} people/km²'.format(self.population_density())
        return output
    
    def population_density(self):
        return self.population/self.area


class Continent:
    ''' Represents a continent '''
    def __init__(self, name, countries):
        self.name = name
        self.countries = countries
        
    def __str__(self):
        output = '\n{}:'.format(self.name)
        for country in self.countries: 
            output += '\n'+str(country)
        return output

def larger_area(a, b):
    if a.area > b.area:
        return a
    elif a.area < b.area:
        return b
    else:
        print('The areas are equal')
        return None


if __name__ == '__main__':

    usa = Country('United States of America', 313914040, 9826675)
    canada = Country('Canada', 34482779, 9984670)
    mexico = Country('Mexico', 127540423, 1964375)
    n_america = Continent('North America', [canada, usa, mexico])
    
    print(n_america)