class Player:
    def __init__(self, name):
        self.name = name
        self.win = False

    @staticmethod
    def take(number_of_cards, pile):
        number_of_cards = min(number_of_cards, len(pile))
        while number_of_cards > 0:
            pile -= 1
            number_of_cards -= 1
        return
