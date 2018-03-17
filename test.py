import functions_for_game


def is_valid(data):
    check_data = dict()
    for i in range(1, 11):
        for j in range(1, 11):

            if data[(i, j)] == '■':

                if data.get((i, j+1)) == '■' \
                   and data.get((i, j-1)) != '■':

                        length = functions_for_game.search_side(data,
                                                                (i, j),
                                                                'right',
                                                                char='■')
                        print(i, j, length)

                # If there is another ship-part under this ship-part and
                # no other ship-part on top of it, get length of
                # vertical ship and create Ship instance.
                elif data.get((i+1, j)) == '■' and \
                        data.get((i-1, j)) != '■':

                        length = functions_for_game.search_side(data,
                                                                (i, j),
                                                                'down',
                                                                char='■')
                        print(i, j, length)

                # If there is no other ship-part around this ship-part,
                # set it's length to 1 and create Ship instance.
                elif data.get((i+1, j)) != '■' and \
                        data.get((i, j+1)) != '■' and \
                        data.get((i-1, j)) != '■' and \
                        data.get((i, j-1)) != '■':

                    length = 1
                    print('1')

                else:
                    length = 0

                if length:
                    if length in check_data:
                        check_data[length] += 1
                    else:
                        check_data[length] = 1

    if len(check_data) == 4:
        if check_data[1] == 4 and check_data[2] == 3 \
                and check_data[3] == 2 and check_data[4] == 1:
            return True
    return False


data_r = functions_for_game.generate_field()
print(functions_for_game.field_to_str(data_r))
is_valid(data_r)
