class Player:
    num_of_players = 0

    def __init__(self, name="Player{}".format(num_of_players)):
        self.__name = name
        Player.num_of_players += 1

    def set_nickname(self):
        nickname = input("If You want, You can enter a nickname: ")
        if nickname:
            self.__name = nickname


    def read_position(self):
        coord = input("Make Your shot (two coords separated by comma): ")
        try:
            self.coord = tuple(map(int, coord.split(',')))
            assert len(self.coord) > 1
            # print(list(filter(lambda x: 10 > x or x < 1, self.coord)))
            assert tuple(filter(lambda x: 1 <= x <= 10, self.coord)) == self.coord
            print(self.coord)
            return self.coord
        except ValueError as v_err:
            print("Bad shot. You entered invalid values.Try again.\n")
            self.read_position()
        except AssertionError:
            print("You entered only one coordinate or coordinates don't \
belong to the field. Try again.\n")
            self.read_position()

    def __str__(self):
        return self.__name
# pl = Player('Lara')
# print(pl)
# pl.read_position()
