from Deck import Deck
from Player import Player
from Circular import Circle


class Game:
    def __init__(self):
        self.number_of_players = int(input("How many players wanna play?\n"))
        self.deck = Deck(self.number_of_players)
        self.players = Circle()
        self.win = False
        self.current_pile = 0
        self.player_turn = None
        for p in range(self.number_of_players):
            player_name = input("player {0} name: ".format(p+1))
            self.players.push(Player(player_name))
        print("Number of players: {}".format(self.number_of_players))
        print("piles are:\n")
        print(*self.deck.deck, sep=' ', end='\n')

    @staticmethod
    def win(winner):
        print(winner.name, "is a winner!")
        return

    def play_turn(self):
        if self.player_turn is None:
            self.player_turn = self.players.top()
        else:
            self.player_turn = self.players.next_node(self.player_turn)
        take = int(input("How much do you wanna take?\n"))
        self.player_turn.value.take(take, self.deck[self.current_pile])
        if self.deck[self.current_pile] <= 0:
            self.current_pile += 1
            if self.current_pile >= len(self.deck.deck):
                self.win = True
        return


def game_finished(game):
    return game.win


def start():
    game = Game()
    while not game_finished(game):
        game.play_turn()
