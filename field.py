import functions_for_game
from ship import Ship


class Field:
    def __init__(self):
        """
        Initialize instance of class. Generate a standart field with ships.
        """
        ships = []
        # Get dict of generated field that consists of coords-keys and values.
        data = functions_for_game.generate_field()
        # Visualize.
        print(functions_for_game.field_to_str(data))

        # Go thruogh all coords.
        for i in range(1, 11):
            ships_row = []
            for j in range(1, 11):

                if data[(i, j)] == '#':
                    # If there is another ship-part after this ship-part and
                    # no other ship-part before it, get length of
                    # horizontal ship and create Ship instance.
                    if data.get((i, j+1)) == '#' \
                       and data.get((i, j-1)) != '#':

                            position = True
                            length = functions_for_game.search_side(data,
                                                                    (i, j),
                                                                    'right',
                                                                    char='#')
                            ship = Ship((i, j), position, length)

                    # If there is another ship-part under this ship-part and
                    # no other ship-part on top of it, get length of
                    # vertical ship and create Ship instance.
                    elif data.get((i+1, j)) == '#' and \
                         data.get((i-1, j)) != '#':

                            position = False
                            length = functions_for_game.search_side(data,
                                                                    (i, j),
                                                                    'down',
                                                                    char='#')
                            ship = Ship((i, j), position, length)
                    # If there is no other ship-part around this ship-part,
                    # set it's length to 1 and create Ship instance.
                    elif data.get((i+1, j)) != '#' and \
                         data.get((i, j+1)) != '#' and \
                         data.get((i-1, j)) != '#' and \
                         data.get((i, j-1)) != '#':

                            position = True
                            length = 1
                            ship = Ship((i, j), position, length)

                    else:
                        if data.get((i, j-1)) == '#':
                            ship = ships_row[-1]
                        elif data.get((i-1, j)):
                            ship = ships[i-2][j-1]


                # If no shup-part was found, create a Ship instance which
                # represents an empty field cell.
                else:
                    length = 'empty'
                    position = 'empty'
                    ship = Ship((i, j), position, length)
                ships_row.append(ship)
            ships.append(ships_row)

        self.__ships = ships
        print(self.__ships)


    def shoot_at(self, coord):
        """
        Add coordinates of hitten ship to class variable of Ship class.
        """
        ship = self.__ships[coord[0]][coord[1]]
        ship.shoot_at(coord)
        # print(self.__ships[coord[0]][coord[1]])

    def field_without_ships(self):
        """
        Return a field without data about ships.
        """
        import string
        letters = string.ascii_uppercase[:10]
        field_no_ships_str = letters + "\n"


        for i in range(1,11):
            row_str = '{} '.format(i-1)
            for j in range(1,11):
                ship = self.__ships[i-1][j-1]
                if ship.is_hitten((i, j)):
                    row_str += 'x '
                else:
                    row_str += '· '
            field_no_ships_str += row_str + '\n'
        print(field_no_ships_str)


    def field_with_ships(self):
        """
        Reuturn field data including information about ships.
        """
        pass
    # def __str__(self):
    #     """
    #     Represent instance of Field class for user.
    #     """
    #     field_str = "on the field (10 * 10): \n  " + "\n  ".join(list(map(str, self.__ships)))
    #
    #     return field_str
f = Field()
f.field_without_ships()
# f.shoot_at((3, 5))
# f.shoot_at((3, 6))
# f.shoot_at((3, 7))
# f.shoot_at((3, 8))





# sgh1 = Ship((2, 1), True, 4)
# sh2 = Ship((3, 2), False, 2)
# f = Field([sgh1, sh2])
# # print(f)


# !!! FIX IS_VALID FUNCTION
