# File: game.py
# This module contains definition of the Game class.


class Game(Field, Player):
    def __init__(fields, players):
        self.__fields = field
        self.__players = players
        self.__current_player = 1

# if (self.bow[0] <= coord[0] <= (self.bow[0] + self.__length[1]) and self.bow[1] <= coord[1] <= (self.bow[1] + self.__length[0])):
#     self.__hit.append(coord)
