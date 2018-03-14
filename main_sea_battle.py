from field import Field
from ship import Ship
from player import Player
from game import Game


name_1 = input("If You want, You can enter a nickname: ")
player_1 = Player(name_1)
name_2 = input("If You want, You can enter a nickname: ")
player_2 = Player(name_2)

print(player_1._Player__name)

sea_battle = Game()
while True:

    sea_battle.read_position()
    if sea_battle._Game__current_player == 0:
        sea_battle._Game__current_player += 1
    else:
        sea_battle._Game__current_player -= 1
    print(sea_battle.field_without_ships())
