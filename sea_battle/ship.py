class Ship:
    hitten = []
    def __init__(self, bow, horizontal, length):
        """
        Initialize class instance:
        -bow (tuple) - coordinates of upper left part of the ship
        -horizontal (bool) - position of the ship
                            True if ship is orisontal
                            False if ship is vertical
        -length (tuple) - vertical and horizontal length of the ship
                         (4, 1) represents a horizontal ship of length 4
                         (1, 4) represents a vertical ship of length 4
        -hit (list) - hitten parts of ships
        """
        self.bow = bow
        self.horizontal = horizontal
        self.__length = length
        self.__hit = []

    def shoot_at(self, coord):
        """
        Add to class variable coordinates of hitten part of the ship.
        """
        Ship.hitten.append(coord)

    def __str__(self):
        return "{position} ship of length {} at {}".format(self.__length,
                                                           self.bow,
                                                           position = "horizontal" if self.horizontal else "vertical")
    def __repr__(self):
        return "{position} ship of length {length} at {}".format(self.bow,
                                                                 length = self.__length,
                                                                 position = "horizontal" if self.horizontal else "vertical")

# self.__length[0] if self.horizontal else self.__length[1],
# sh = Ship((1, 3), True, (4, 1))
# sh.shoot_at((1, 5))
# print(Ship.hitten)
