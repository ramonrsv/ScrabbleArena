from lib.position import ClassicPositionProperty
from .board import BoardConfiguration
from .position import Position
from .tile import LetterDistribution, TileDistribution

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

Words_with_friends_board_configuration = BoardConfiguration.from_corners_symmetry(15, 15, [
    Position(4, 1, ClassicPositionProperty.W3), Position(7, 1, ClassicPositionProperty.L3),
    Position(3, 2, ClassicPositionProperty.L2), Position(6, 2, ClassicPositionProperty.W2),
    Position(2, 3, ClassicPositionProperty.L2), Position(5, 3, ClassicPositionProperty.L2),
    Position(1, 4, ClassicPositionProperty.W3), Position(4, 4, ClassicPositionProperty.L3),
    Position(8, 4, ClassicPositionProperty.W2),
    Position(3, 5, ClassicPositionProperty.L2), Position(7, 5, ClassicPositionProperty.L2),
    Position(2, 6, ClassicPositionProperty.W2), Position(6, 6, ClassicPositionProperty.L3),
    Position(1, 7, ClassicPositionProperty.L3), Position(5, 7, ClassicPositionProperty.L2),
    Position(4, 8, ClassicPositionProperty.W2), Position(8, 8, ClassicPositionProperty.CENTER)
])

Words_with_friends_fast_play_board_configuration = BoardConfiguration.from_corners_symmetry(11, 11, [
    Position('A', 1, ClassicPositionProperty.L3), Position('C', 1, ClassicPositionProperty.W3),
    Position('B', 2, ClassicPositionProperty.W2), Position('F', 2, ClassicPositionProperty.W2),
    Position('A', 3, ClassicPositionProperty.W3), Position('C', 3, ClassicPositionProperty.L2),
    Position('E', 3, ClassicPositionProperty.L2),
    Position('D', 4, ClassicPositionProperty.L3),
    Position('C', 5, ClassicPositionProperty.L2),
    Position('B', 5, ClassicPositionProperty.W2)
])

Standard_player_tray_size = 10
