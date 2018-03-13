from ship import Ship
import functions_for_game
import random

class Field:
    def __init__(self):
        """
        Initialize instance of class. Generate a standart field with ships.
        """
        ship_res = []
        ships = []
        # Get dict of coords and the value.
        data = functions_for_game.generate_field()
        # Visualize.
        print(functions_for_game.field_to_str(data))

        for i in range(1, 11):
            for j in range(1, 11):
                if data[(i, j)] == '#':

                    if data.get((i, j+1)) == '#' and  data.get((i, j-1)) != '#':
                        print("checking", (i,j))
                        length = functions_for_game.search_side(data, (i, j), 'right', char='#')
                        position = True
                    elif data.get((i+1, j)) == '#' and  data.get((i-1, j)) != '#':
                        print("checking", (i,j))
                        length = functions_for_game.search_side(data, (i, j), 'down', char='#')
                        position = False
                    elif data.get((i+1, j)) != '#' and \
                            data.get((i, j+1)) != '#' and \
                            data.get((i-1, j)) != '#' and \
                            data.get((i, j-1)) != '#':
                        length = 1
                        position = True
                else:
                    length = None
                    position = None
                if length:
                    print(Ship((i, j), position, length))
                ships.append(Ship((i, j), position, length))
                # print(Ship((i, j), position, length))
            ship_res.append(ships)
        print(len(ship_res))
        print("!!!")

        #self.__ships = ships
    def shoot_at(self, coord):
        """
        Add coordinates of hitten ship to class variable of Ship class.
        """
        #self.__ships[coord[0]][coord[1]].__hit.append(coord)
        pass

    def field_without_ships(self):
        """
        Return a field without data about ships.
        """
        pass

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
# sgh1 = Ship((2, 1), True, 4)
# sh2 = Ship((3, 2), False, 2)
# f = Field([sgh1, sh2])
# # print(f)
