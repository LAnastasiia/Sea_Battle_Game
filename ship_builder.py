import random
import string

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
    directions = ['left', 'right', 'up', 'down']
    while True:
        coord = (random.randint(1,10), random.randint(1,10))
        direct = random.choice(directions)
        checked_data = check_zone(data, data_with_ships, coord, direct, ship_lengh)
        if checked_data:
            data.update(checked_data)
            break


# build_ship(generate_data(), 4)

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
    print(data_str)
    return data_str

data_with_ships = list()
data = generate_field()
field_to_str(data)
