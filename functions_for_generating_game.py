# File: functions_for_generating_game.py
# This module contains functions needed for generating and checking the
# sea-battle field for Sea Battle game.
import string
import random


def read_field(file_name):
    """
    (str) -> (dict)

    This function reads info about sea-battle field from file and represents
    it as list of tuples with coordinates and symbols.
    """
    with open(file_name, 'r', encoding='utf-8', errors='ignore') as field_file:
        data = dict()
        line_num = 1

        for line in field_file:
            num = 1
            line = line.strip('\n')
            for symb in line:
                data[(line_num, num)] = symb
                num += 1
            line_num += 1
        return data


def has_ship(data, coord, char='#'):
    """
    (dict) -> (bool)
    This function checks presence of ship on certain coordinates.
    """
    for key in data:
        if key == coord:
            if data[key] == char:
                return True
    return False





def ship_size(data, coord, char='#'):
    """
    (dict, tuple) -> (int)

    This function searches the length of ship according to given coordinates
    and returnes it's size. To search for parts of ship in different
    directions, search_side(data, coord, side) function is used.

    If there's no ship in these coordinates, returns 0.
    """
    ship_len = 0

    if has_ship(data, coord, char):
        ship_len = 1
        if search_side(data, coord, 'left'):
            ship_len += (search_side(data, coord, 'left') +
                         search_side(data, coord, 'right'))

        else:
            ship_len += (search_side(data, coord, 'up') +
                        (search_side(data, coord, 'down')))
        return ship_len

    return 0


def is_valid(data):
    """
    (data) -> (bool)
    This function checks whether given sea-battle field is valid. It checks
    size of field (so that it should be 10 * 10), length of all ships
    (so they all must be less than 5), checks amount of
    ships for different length values (so that there must be only 1 ship of
    length 4; 2 ships of length 3; 3 ships of length 2 and 4 ships of
    length 1). If something is wrong, it prints out a message about error and
    returnes False. If everything is valis, - returns True.
    """
    if (10, 10) in data:
        check_size_dict = dict()
        for key_coord in data:
            ship_len = ship_size(data, key_coord)
            if ship_len < 5:
                if ship_len in check_size_dict:
                    check_size_dict[ship_len] += 1
                else:
                    check_size_dict[ship_len] = 1
            else:
                print("Wrong length of ship. All shipps must be less than 5.")
        if (check_size_dict[4] == 4 and check_size_dict[3] == 6 and
            check_size_dict[2] == 6 and check_size_dict[1] == 4):

            return True
        else:
            print("Wrong amount or(and) length of ships.")
            return False
    else:
        print("Wrong size of field. Expected: 10 * 10.")
        return False


def field_to_str(data):
    """
    (dict) -> (str)

    This function converts dict (which contains data about sea-battle field)
    to str, so that it can be represented on the screen.
    """
    num_markup = list([str(i) for i in range(1, 11)])
    letters = [lett for lett in string.ascii_uppercase[:10]]
    data_str = '    ' + "  ".join(letters)
    for el in sorted(list(data)):
        lett_ind = el[0]
        el_str = "  {}".format(data[el])
        if el[1] == 1:
            el_str = '\n' + '{0:2}'.format(num_markup[lett_ind-1]) + el_str
        data_str += el_str
    return data_str


def generate_data():
    """
    () -> (dict)
    This function generates data about simple sea-battle field with '·'.
    """
    data_gen = dict()
    for lett_ind in range(1, 11):
        for num in range(1, 11):
            data_gen[(num, lett_ind)] = '·'
            num += 1
        lett_ind += 1
    return data_gen



def search_side(data, coord, side, char='#'):
    """
    (dict, tuple, str) -> (int)
    This function searches for ship body in one given direction (starting
    from certain coordinates) and returns it's length.
    """
    ship_length = 1
    while True:
        if side == 'up':
            try_coord = (coord[0]-1, coord[1])
        elif side == 'down:':
            try_coord = (coord[0]+1, coord[1])
        elif side == 'left':
            try_coord = (coord[0], coord[1]-1)
        else:
            try_coord = (coord[0], coord[1]+1)

        if try_coord in data:
            if has_ship(data, try_coord, char):
                ship_length += 1
                coord = try_coord
            else:
                break
        else:
            break
    return ship_length


def check_zone(data, data_with_ships, coord, direct, ship_lengh):
    data_try = dict()
    if data[coord] == '#' or coord in data_with_ships:
        return False
    data_try[coord] = '#'
    ship_len = 1
    while ship_len < ship_lengh:
        if direct == 'up':
            new_coord = (coord[0]-1, coord[1])
        elif direct == 'down':
            new_coord = (coord[0]+1, coord[1])
        elif direct == 'left':
            new_coord = (coord[0], coord[1]-1)
        else:
            new_coord = (coord[0], coord[1]+1)

        if (new_coord in data_with_ships) or (new_coord not in data):
            return False

        data_try[new_coord] = '#'
        ship_len += 1
        coord = new_coord


    for coords in data_try:
        if direct == 'up' or direct == 'down':
            data_with_ships.extend([coords, (coords[0], coords[1]+1),
                                (coords[0], coords[1]-1)])
        else:
            data_with_ships.extend([coords, (coords[0]+1, coords[1]),
                                (coords[0]-1, coords[1])])

    if direct == 'up' or direct == 'down':
        sorted_data_try = sorted(data_try, key = lambda x: x[0], reverse=False)
        min_ship_coord = sorted_data_try[0]
        print("min coord:", min_ship_coord)
        print("max sort", sorted_data_try)
        max_ship_coord = sorted_data_try[-1]
        print(max_ship_coord)
        data_with_ships.extend([(min_ship_coord[0]-1,min_ship_coord[1]),
                               (min_ship_coord[0]-1, min_ship_coord[1]-1),
                               (min_ship_coord[0]-1, min_ship_coord[1]+1),
                               (max_ship_coord[0]+1, max_ship_coord[1]),
                               (max_ship_coord[0]+1, max_ship_coord[1]-1),
                               (max_ship_coord[0]+1, max_ship_coord[1]+1)])
    elif direct == 'left' or direct == 'right':
        sorted_data_try = sorted(data_try, key = lambda x: x[1], reverse=False)
        min_ship_coord = sorted_data_try[0]
        print("min coord:", min_ship_coord)
        print("max sort", sorted_data_try)
        max_ship_coord = sorted_data_try[-1]
        print("max coord", max_ship_coord)
        data_with_ships.extend([(min_ship_coord[0],min_ship_coord[1]-1),
                               (min_ship_coord[0]-1, min_ship_coord[1]-1),
                               (min_ship_coord[0]+1, min_ship_coord[1]-1),
                               (max_ship_coord[0], max_ship_coord[1]+1),
                               (max_ship_coord[0]-1, max_ship_coord[1]+1),
                               (max_ship_coord[0]+1, max_ship_coord[1]+1)])

    print("data_try:", data_try)
    print("data with ships:", data_with_ships)
    return (data_try)

def build_ship(data, ship_lengh):
    """
    This function builds ship of given length in randomly chosen coordinate
    and direction.
    """
    directions = ['left', 'right', 'up', 'down']
    while True:
        coord = (random.randint(1,10), random.randint(1,10))
        direct = random.choice(directions)
        checked_data = check_zone(data, data_with_ships, coord, direct,
                                  ship_lengh)
        if checked_data:
            data.update(checked_data)
            break

def generate_field():
    """
    This function generates a 10 * 10 sea-battle-field with valid amount ships
    using functions generate_data() and build_ship(data_gen, size).
    """
    num_of_ships = 1
    data = generate_data()
    length = 4
    for _ in range(4):
        for i in range(num_of_ships):
            build_ship(data, length)
        length -= 1
        num_of_ships += 1
    return data

data_with_ships = list()
data = generate_data()
print(field_to_str(generate_field()))
