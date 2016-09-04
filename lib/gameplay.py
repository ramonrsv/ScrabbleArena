from .position import PosProperty, Position
from .board import BoardContainer


class GameplayPosition(Position):
    def __init__(self, x, y, pos_property=PosProperty.normal):
        Position.__init__(self, x, y, pos_property)


class GameplayBoard(BoardContainer):
    def __init__(self, board_configuration):
        BoardContainer.__init__(self, board_configuration)

    def _create_position_object(self, position):
        """Overloading BoardContainer definition to return GameplayPosition instead"""
        return GameplayPosition(position.x, position.y, position.property)
