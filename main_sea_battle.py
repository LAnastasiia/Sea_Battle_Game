from field import Field
from ship import Ship
from player import Player
from game import Game



sea_battle = Game()
while True:
    # Display field with no ships.
    print(sea_battle.field_without_ships())
    print(sea_battle._Game__players[sea_battle._Game__current_player])
    # Read coordinates of the shot.
    sea_battle.read_position()

    # Change player.
    if sea_battle._Game__current_player == 0:
        sea_battle._Game__current_player += 1
    else:
        sea_battle._Game__current_player -= 1
