'''
	cards.py
	- Class definitions from Think Python Chapter 18
	- Daniel Thomas
	- Dec. 2, 2017
'''

import random

class Card:
    ''' Represents a standard playing card '''

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
            'Jack', 'Queen', 'King']
    
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
    
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2
    
class Deck:
    ''' Represents a deck of playing cards '''
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)
    
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

class Hand(Deck):
    ''' Represents a hand of playing cards '''
    
    def __init__(self, label =''):
        self.cards = []
        self.label = label
    
    

if __name__ == '__main__':
    
    card1 = Card(2, 11)
    card2 = Card(2, 1)
    print('%s < %s: %s' %(card2, card1, (card2 < card1)))
    
    deck = Deck()
    deck.shuffle()
    print(deck)