from lib.board import BoardConfiguration
from lib.position import Position, ClassicPositionProperty


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
