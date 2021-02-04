import random


class Deck:
    def __init__(self, number_of_players=2):
        self.deck = [1]
        self.number_of_piles = max(random.randrange(1, 100, 1), number_of_players) + 1
        while len(self.deck) < self.number_of_piles:
            self.deck.append(random.randrange(1, 100, 1))
