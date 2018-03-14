# File: game.py
# This module contains definition of the Game class.


class Game(Field, Player):
    def __init__(fields, players):
        """
        Initialize instance of Game class.

        :field: (list) array of fields;
        :players: (list) array of players;
        :current_player: (int) index of the current player.
        """
        self.__field = fields
        self.__players = players
        self.__current_player = 1

    def field_without_ships(self, index):
        """
        Show a field (chosen from the field list by index) without ships but
        with shots marked.
        """

    def field_with_ships(self, index)
