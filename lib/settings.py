from .tile import LetterDistribution, TileDistribution
from .position import PositionProperty, Position
from .board import BoardConfiguration


English_classic_letter_distribution = LetterDistribution(
    blank='_',
    distribution={
        '_': 0,
        'A': 1,
        'B': 3,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 4,
        'G': 2,
        'H': 4,
        'I': 1,
        'J': 8,
        'K': 5,
        'L': 1,
        'M': 3,
        'N': 1,
        'O': 1,
        'P': 3,
        'Q': 10,
        'R': 1,
        'S': 1,
        'T': 1,
        'U': 1,
        'V': 4,
        'W': 4,
        'X': 8,
        'Y': 4,
        'Z': 10})

English_classic_100_tile_distribution = TileDistribution(
    letter_distribution=English_classic_letter_distribution,
    tile_distribution={
        English_classic_letter_distribution.BLANK: 2,
        'A': 9,
        'B': 2,
        'C': 2,
        'D': 4,
        'E': 12,
        'F': 2,
        'G': 3,
        'H': 2,
        'I': 9,
        'J': 1,
        'K': 1,
        'L': 4,
        'M': 2,
        'N': 6,
        'O': 8,
        'P': 2,
        'Q': 1,
        'R': 6,
        'S': 4,
        'T': 6,
        'U': 4,
        'V': 2,
        'W': 2,
        'X': 1,
        'Y': 2,
        'Z': 1})


class EnglishClassicPositionProperty(PositionProperty):
    normal = 0
    CENTER = 1
    DL = 2
    TL = 3
    DW = 4
    TW = 5
    L2 = DL
    L3 = TL
    W2 = DW
    W3 = TW
    W4 = 6

    @classmethod
    def _letter_multiplier_dict(cls):
        return cls._get_full_letter_multiplier_dict(
            {cls.DL: 2, cls.TL: 3,
             cls.L2: 2, cls.L3: 3}, default_value=1)

    @classmethod
    def _word_multiplier_dict(cls):
        return cls._get_full_word_multiplier_dict(
            {cls.DW: 2, cls.TW: 3,
             cls.W2: 2, cls.W3: 3, cls.W4: 4}, default_value=1)


Words_with_friends_board_configuration = BoardConfiguration.from_corners_symmetry(15, 15, [
    Position(4, 1, EnglishClassicPositionProperty.W3), Position(7, 1, EnglishClassicPositionProperty.L3),
    Position(3, 2, EnglishClassicPositionProperty.L2), Position(6, 2, EnglishClassicPositionProperty.W2),
    Position(2, 3, EnglishClassicPositionProperty.L2), Position(5, 3, EnglishClassicPositionProperty.L2),
    Position(1, 4, EnglishClassicPositionProperty.W3), Position(4, 4, EnglishClassicPositionProperty.L3),
    Position(8, 4, EnglishClassicPositionProperty.W2),
    Position(3, 5, EnglishClassicPositionProperty.L2), Position(7, 5, EnglishClassicPositionProperty.L2),
    Position(2, 6, EnglishClassicPositionProperty.W2), Position(6, 6, EnglishClassicPositionProperty.L3),
    Position(1, 7, EnglishClassicPositionProperty.L3), Position(5, 7, EnglishClassicPositionProperty.L2),
    Position(4, 8, EnglishClassicPositionProperty.W2), Position(8, 8, EnglishClassicPositionProperty.CENTER)
])

Words_with_friends_fast_play_board_configuration = BoardConfiguration.from_corners_symmetry(11, 11, [
    Position('A', 1, EnglishClassicPositionProperty.L3), Position('C', 1, EnglishClassicPositionProperty.W3),
    Position('B', 2, EnglishClassicPositionProperty.W2), Position('F', 2, EnglishClassicPositionProperty.W2),
    Position('A', 3, EnglishClassicPositionProperty.W3), Position('C', 3, EnglishClassicPositionProperty.L2),
    Position('E', 3, EnglishClassicPositionProperty.L2),
    Position('D', 4, EnglishClassicPositionProperty.L3),
    Position('C', 5, EnglishClassicPositionProperty.L2),
    Position('B', 5, EnglishClassicPositionProperty.W2)
])

Standard_player_tray_size = 10
