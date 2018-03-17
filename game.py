# File: game.py
# This module contains definition of the Game class.
from field import Field
from ship import Ship
from player import Player
import functions_for_game


class Game:
    def __init__(self, num_of_players):
        """
        Initialize instance of Game class.

        :field: (list) array of fields;
        :players: (list) array of players;
        :current_player: (int) index of the current player.
        """
        self.num_of_players = num_of_players
        # Generate a list of Players.
        self.__players = [Player() for i in range(self.num_of_players)]
        # Give a chance to pick up a nickname for every player.
        for pl in self.__players:
            pl.set_nickname()

        # Generate Field(s) according to num_of_players.
        self.__field = [Field() for i in range(self.num_of_players)]
        self.__current_player = 0


    def read_position(self):
        shot = self.__players[self.__current_player].read_position()
        self.__field[self.__current_player].shoot_at(shot)

    def field_without_ships(self):
        """
        Show a field (chosen from the field list by index) without ships but
        with shots marked on it.
        """
        field_shots = self.__field[self.__current_player].field_without_ships()
        return field_shots

    def field_with_ships(self):
        """
        Show a field (chosen from the field list by index) with both ships
        and shots marked on it.
        """
        field_str = self.__field[self.__current_player].field_with_ships()
        return field_str
