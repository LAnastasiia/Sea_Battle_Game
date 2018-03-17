# Generate game case when there is only one player vs program.
if self.num_of_players == 1:
    self.__players = [Player(), Player()]
    self.__players.set_nickname()
    if field_file_path:
        try:
            assert os.path.isfile(field_file_path)
            field = functions_for_game.read_field()
            assert functions_for_game.is_valid(field)
            self.__field = field
        except AssertionError:
            print("There is no file named {} or this file \
contains invalid field. Fix it to play.".format(field_file_path))
