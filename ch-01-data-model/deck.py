from collections import namedtuple
from random import choice

Card = namedtuple('Card', ('rank', 'suit'))

class Deck:
    ranks = [str(r) for r in range(2, 11)] + list('JQKA')
    suits = 'spades hearts diamonds clubs'.split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) 
            for rank in self.ranks 
            for suit in self.suits
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

deck = Deck()

print('len', len(deck))

suit_values = {
    "spades": 3,
    "hearts": 2,
    "diamonds": 1,
    "clubs": 0
}

def spades_high(card):
    rank = Deck.ranks.index(card.rank)
    return rank * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card, spades_high(card))

print('random card', choice(deck))
