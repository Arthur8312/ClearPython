# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:09:41 2021

@author: arthur
"""

import collections
from random import choice
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]
    
    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, position):
        return self.cards[position]
    

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck)) #Class 中實做 __len__
print(deck[0]) #Class 中實做__getitem__
print(deck[-1]) 

for card in deck: #Class 中實做__getitem__ deck變成可以迭代
    print(card)

print(choice(deck)) #實做隨機抽一張

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)