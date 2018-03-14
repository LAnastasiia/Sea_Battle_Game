class Ship:
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
        self.__hit.append(coord)

    def is_hitten(self, coord):
        """
        Check if certain coordinates belong to the hitten part of the ship.
        Return True if iven coord are in hit list of the Ship instance.
        Else return false.
        """
        if coord in self.__hit:
            return True
        return False

    def has_coord(self, coord):
        """
        Check whether certain coordinates are a part of a ship.
        """
        if (self.bow[0] < coord[0] < self.bow[0] + length[0]) \
            and (self.bow[1] < coord[1] < self.bow[1] + length[1]):

            return True
        return False

    def __str__(self):
        """
        Represent an instance for a user.
        """
        if self.__length == "empty":
            return "empty field on {}".format(self.bow)
        elif self.__length == 1:
            return "ship of length {length} at {}".format(self.bow,
                                                          length = self.__length)
        #horizontal = "horizontal" if self.horizontal else "vertical" "" if self.__length == 1 else ""
        return "{position} ship of length {} at {}".format(self.__length,
                                                           self.bow,
                                                           position="horizontal" if self.horizontal else "vertical")

    def __repr__(self):
        """
        Represent an instance for a programmer.
        """
        if self.__length == "empty":
            return "empty field on {}".format(self.bow)
        elif self.__length == 1:
            return "ship of length {length} at {}".format(self.bow,
                                                          length = self.__length)

        return "{position} ship of length {length} at {}".format(self.bow,
                                                                 length = self.__length,
                                                                 position = "horizontal" if self.horizontal else "vertical")

# self.__length[0] if self.horizontal else self.__length[1],
sh = Ship((1, 3), True, (4, 1))
sh.shoot_at((1, 5))
