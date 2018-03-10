class Player:
    num_of_players = 0
    def __init__(self, name="Player{}".format(num_of_players)):
        self.__name = name
        Player.num_of_players += 1
    # def __str__(self):
    #     return "Player{} - {}".format(Player.num_of_players, self.__name)
    # def __repr__(self):
    #     return self.__name
    def read_position(self):
        coord = input("Make Your shot (two coords separated by comma): ")
        try:
            self.coord = tuple(map(int, coord.split(',')))
            assert len(self.coord) > 1
            print(self.coord)
            return coord
        except ValueError as v_err:
            print("Bad shot. You entered invalid values.Try again.\n")
            self.read_position()
        except AssertionError:
            print("You entered only one coordinate. Try again.\n")
            self.read_position()
        # except EOFError:
        #     print("You can't miss Your turn. If You want to quit, enter QUIT")
        #     self.read_position()
pl = Player('Lara')
print(pl)
pl.read_position()
