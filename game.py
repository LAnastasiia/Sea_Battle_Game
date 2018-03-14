# File: game.py
# This module contains definition of the Game class.
from field import Field
from ship import Ship
from player import Player

class Game:
    def __init__(self):
        """
        Initialize instance of Game class.

        :field: (list) array of fields;
        :players: (list) array of players;
        :current_player: (int) index of the current player.
        """
        self.__field = [Field(), Field()]
        self.__players = [Player(), Player()]
        self.__current_player = 0

    def field_without_ships(self):
        """
        Show a field (chosen from the field list by index) without ships but
        with shots marked on it.
        """
        field_shots = self.__field[self.__current_player].field_without_ships()
        self.__current_player += 1
        return field_shots

    def field_with_ships(self):
        """
        Show a field (chosen from the field list by index) with both ships
        and shots marked on it.
        """
        field_str = self.__field[self.__current_player].field_with_ships()
        return field_str

g = Game()
print(g.field_with_ships())
