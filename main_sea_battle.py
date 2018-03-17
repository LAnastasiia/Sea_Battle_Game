from field import Field
from ship import Ship
from player import Player
from game import Game
import functions_for_game

while True:
    # Get the number of players.
    try:
        num_of_players = int(input("Enter a number of players: "))
        assert num_of_players > 1
        break
    except ValueError:
        print("Invalid value. Please, check Your input and try again.")
    except AssertionError:
        print("You can only have a greater than 1 number of players. \
Try again.")

# Generate the game.
sea_battle = Game(num_of_players)
while True:
    print('\n\n')
    # Display field with no ships.
    print(sea_battle.field_without_ships())
    print(sea_battle._Game__players[sea_battle._Game__current_player])
    # Read coordinates of the shot.
    sea_battle.read_position()
    # Check for a winner.
    if functions_for_game.is_valid(
            sea_battle._Game__field[sea_battle._Game__current_player]._Field__ships,
            char='⛒'):
        print("Congratulations!",
              sea_battle._Game__current_player._Player__name,
              "You won!")
    else:
        # Change player.
        sea_battle._Game__current_player += 1
        # If all players made their shots, start new sequence of turns.
        if sea_battle._Game__current_player == len(sea_battle._Game__players):
            sea_battle._Game__current_player = 0
