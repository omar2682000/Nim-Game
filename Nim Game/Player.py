class Player:
    def __init__(self, name):
        self.name = name
        self.win = False

    @staticmethod
    def take(number_of_cards, pile):
        number_of_cards = min(number_of_cards, pile)
        pile -= number_of_cards
        return
