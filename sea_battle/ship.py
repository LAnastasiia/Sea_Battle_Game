class Ship:
    hitten = []
    def __init__(self, bow, horizontal, length):
        """
        Initialize class instance:
        bow (tuple) - coordinates of upper left part of the ship
        horizontal (bool) - position of the ship
        length (tuple) - vertical and horizontal length of the ship

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


sh = Ship((1, 3), True, (4, 1))
sh.shoot_at((1, 5))
print(Ship.hitten)
