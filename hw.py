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


def has_ship(data, coord):
    """
    (dict) -> (bool)
    This function checks presence of ship on certain coordinates.
    """
    for key in data:
        if key == coord:
            if data[key] == '*':
                return True
            else:
                return False


def search_side(data, coord, side):
    """
    (dict, tuple, str) -> (int)
    This function searches for ship body in one given direction (starting
    from certain coordinates) and returns it's length.
    """
    ship_length = 0
    while True:
        if side == 'up':
            try_coord = (coord[0]-1, coord[1])
        elif side == 'down:':
            try_coord = (coord[0]+1, coord[1])
        elif side == 'left':
            try_coord = (coord[0], coord[1]-1)
        else:
            try_coord = (coord[0], coord[1]+1)

        if has_ship(data, try_coord):
            ship_length += 1
            coord = try_coord
            continue

        break
    return ship_length


def ship_size(data, coord):
    """
    (dict, tuple) -> (int)

    This function searches the length of ship according to given coordinates
    and returnes it's size. To search for parts of ship in different
    directions, search_side(data, coord, side) function is used.

    If there's no ship in these coordinates, returns 0.
    """
    ship_len = 0

    if has_ship(data, coord):
        ship_len = 1
        if search_side(data, coord, 'left'):
            ship_len += (search_side(data, coord, 'left') +
                         search_side(data, coord, 'right'))

        else:
            ship_len += (search_side(data, coord, 'up') +
                        (search_side(data, coord, 'down')))
        return ship_len

    else:
        print("No ship found on {}".format(coord))
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


def check_zone(data, coord, character):
    """
    (dict, tuple, str) -> (int)
    This function checks, how many certain characters there are around given
    coordinate. Returns amount of found characters.
    """
    count = 0
    for (x,y) in {(0,0), (1,0), (-1,0), (0, 1), (0, -1)}:
        if (coord[0]+x, coord[1]+y) in data:
            if data[coord[0]+x, coord[1]+y] == '#':
                count += 1
    return count


def build_ship(data_gen, size):
    """
    This function builds a ship of given size on the field, according
    to data_gen info. Returns modyfied (with instrted values of some cells)
    data_gen dict.
    """
    while True:
        # Choose starting coord randomly.
        coord = (random.randint(1, 10), random.randint(1, 10))
        # Assign coord values to ship_coord to keep original coords unchanged.
        ship_coord = coord
        print("ship:", ship_coord)
        # Check zone around coord.
        if check_zone(data_gen, coord, '#') == 0:
            data_gen[coord] = '#'
            ship_len = 1
            break

    # Pick a direction randomly.
    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)

    while ship_len < size:
        # Check border positions. Change direction on the end of the field.
        if direction == 'up' and coord[0] == 1:
            direction = 'down'
            coord = ship_coord

        elif direction == 'down' and coord[0] == 10:
            direction = 'up'
            coord = ship_coord

        elif direction == 'left' and coord[1] == 1:
            direction = 'right'
            coord = ship_coord

        elif direction == 'right' and coord[1] == 10:
            direction = 'left'
            coord = ship_coord


        # Set new_coord according to the direcion of building.
        if direction == 'up':
            new_coord = (coord[0]-1, coord[1])

        elif direction == 'down':
            new_coord = (coord[0]+1, coord[1])

        elif direction == 'left':
            new_coord = (coord[0], coord[1]-1)

        elif direction == 'right':
            new_coord = (coord[0], coord[1]+1)

        # Check if there are no other ships on neighbour cells.
        if (new_coord in data_gen and check_zone(data_gen, new_coord, '#')) == 1:
            # Add ship part on the field-cell.
            data_gen[new_coord] = '#'
            print(new_coord)
            coord = new_coord
            ship_len += 1

    print(field_to_str(data_gen))


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
generate_field()
