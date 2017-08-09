from lib.letter_value_map import LetterValueMap
from lib.tile import TileBagDistribution
from lib.board import BoardConfiguration


class GameSettings:
    def __init__(self, letter_value_map, tile_bag_distribution, board_configuration, player_tray_size):
        assert isinstance(letter_value_map, LetterValueMap), \
            "letter_value_map must be LetterValueMap type"
        assert isinstance(tile_bag_distribution, TileBagDistribution), \
            "tile_bag_distribution must be TileBagDistribution type"
        assert isinstance(board_configuration, BoardConfiguration), \
            "board_configuration must be BoardConfiguration type"
        assert isinstance(player_tray_size, int) and player_tray_size > 0, \
            "player_tray_size must be a positive integer"
        assert letter_value_map.all_letters() == tile_bag_distribution.all_letters(), \
            "tile_bad_distribution must have been initialized with letter_value_map - they must have the same letters"

        self._letter_value_map = letter_value_map
        self._tile_bag_distribution = tile_bag_distribution
        self._board_configuration = board_configuration
        self._player_tray_size = player_tray_size

    @property
    def letter_value_map(self):
        return self._letter_value_map

    @property
    def tile_bag_distribution(self):
        return self._tile_bag_distribution

    @property
    def board_configuration(self):
        return self._board_configuration

    @property
    def player_tray_size(self):
        return self._player_tray_size
