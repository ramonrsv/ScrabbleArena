from .position import Position
from .dimension_coordinate_properties import DimensionProperty


class BoardContainer(DimensionProperty):
    def __init__(self, board_configuration):
        DimensionProperty.__init__(self, board_configuration.width, board_configuration.height)
        self.__config = board_configuration
        self.__positions = self._make_all_positions_dict(board_configuration)
        self.__coo_list = list(self.__positions.keys())
        self.__coo_list.sort()

    @staticmethod
    def _create_position_object(position):
        """Can be overloaded to create a different type of Position object (which should inherit from Position)"""
        return Position(position.x, position.y, position.property)

    @classmethod
    def _make_all_positions_dict(cls, board_configuration):
        """Make a (x,y): Position dictionary of all the special positions, and fill in the rest"""
        ret = {}
        for pos in board_configuration.special_positions:
            ret[pos.coo] = cls._create_position_object(pos)
        for y in range(1, board_configuration.height + 1):
            for x in range(1, board_configuration.width + 1):
                if (x, y) not in ret:
                    ret[(x, y)] = cls._create_position_object(Position(x, y))
        return ret

    def positions(self):
        """Iterate over all positions"""
        for coo in self.__coo_list:
            yield self.__positions[coo]

    def get_position(self, coo):
        """Retrieve a position from a coordinate tuple (x,y)"""
        return self.__positions.get(Position(coo[0], coo[1]).coo, None)  # Accept ('A',1) form, helped by Position
