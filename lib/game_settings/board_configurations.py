from lib.board import BoardConfiguration
from lib.position import Position, ClassicPositionAttribute


Words_with_friends_board_configuration = BoardConfiguration.from_corners_symmetry(15, 15, [
    Position(4, 1, ClassicPositionAttribute.W3), Position(7, 1, ClassicPositionAttribute.L3),
    Position(3, 2, ClassicPositionAttribute.L2), Position(6, 2, ClassicPositionAttribute.W2),
    Position(2, 3, ClassicPositionAttribute.L2), Position(5, 3, ClassicPositionAttribute.L2),
    Position(1, 4, ClassicPositionAttribute.W3), Position(4, 4, ClassicPositionAttribute.L3),
    Position(8, 4, ClassicPositionAttribute.W2),
    Position(3, 5, ClassicPositionAttribute.L2), Position(7, 5, ClassicPositionAttribute.L2),
    Position(2, 6, ClassicPositionAttribute.W2), Position(6, 6, ClassicPositionAttribute.L3),
    Position(1, 7, ClassicPositionAttribute.L3), Position(5, 7, ClassicPositionAttribute.L2),
    Position(4, 8, ClassicPositionAttribute.W2), Position(8, 8, ClassicPositionAttribute.CENTER)
])

Words_with_friends_fast_play_board_configuration = BoardConfiguration.from_corners_symmetry(11, 11, [
    Position('A', 1, ClassicPositionAttribute.L3), Position('C', 1, ClassicPositionAttribute.W3),
    Position('B', 2, ClassicPositionAttribute.W2), Position('F', 2, ClassicPositionAttribute.W2),
    Position('A', 3, ClassicPositionAttribute.W3), Position('C', 3, ClassicPositionAttribute.L2),
    Position('E', 3, ClassicPositionAttribute.L2),
    Position('D', 4, ClassicPositionAttribute.L3),
    Position('C', 5, ClassicPositionAttribute.L2),
    Position('B', 5, ClassicPositionAttribute.W2)
])
