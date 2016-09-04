from .position import Position
from .dimension_coordinate_properties import DimensionProperty


class BoardConfiguration(DimensionProperty):
    def __init__(self, width, height, special_positions=None):
        DimensionProperty.__init__(self, width, height)
        self.__special_positions = []
        self.special_positions = special_positions if special_positions else []

    @property
    def special_positions(self):
        return self.__special_positions

    @special_positions.setter
    def special_positions(self, special_positions):
        if not isinstance(special_positions, list):
            raise TypeError("special_positions should be a list of Position's")
        seen = set()
        for pos in special_positions:
            if not isinstance(pos, Position):
                raise TypeError("special_positions should be a list of Position's")
            if pos.coo in seen or seen.add(pos.coo):
                raise ValueError("there cannot be repeated positions: " + str(pos.coo))
            if pos.x > self.width or pos.y > self.height:
                raise ValueError("out of bounds position: " + str(pos.coo) +
                                 " - " + str(self.width, self.height) + " dimensions")
        self.__special_positions = special_positions

    def set_special_positions(self, special_positions):
        self.special_positions = special_positions

    @staticmethod
    def _mirror_position(pos, direction, width, height):
        assert direction in ['x', 'y'], "bad direction '" + str(direction) + "'"  # TODO: Implement diagonal direction
        ret = Position(width - pos.x + 1 if direction == 'x' else pos.x,
                       height - pos.y + 1 if direction == 'y' else pos.y, pos.property)
        return ret if ret != pos else None

    @classmethod
    def from_corners_symmetry(cls, width, height, special_positions):
        """Only one corner has to be defined - common row/column has to be defined for odd width/height.
        All positions will be mirrored, and there are no checks that they are all in one corner"""
        config = cls(width, height, special_positions)  # Does error checking on parameters
        if len(special_positions) == 0:
            return config

        # _mirror_position return None if it can't be mirrored, ensure it is not appended to the list
        special_positions += [pos for pos in
                              [cls._mirror_position(pos, 'x', width, height) for pos in special_positions]
                              if pos]
        special_positions += [pos for pos in
                              [cls._mirror_position(pos, 'y', width, height) for pos in special_positions]
                              if pos]
        seen = set()
        for pos in special_positions:
            if pos.coo in seen or seen.add(pos.coo):
                raise ValueError("duplicate position: " + str(pos.coo) +
                                 " - duplicate positions result from not defining all special positions in one corner")
        return BoardConfiguration(width, height, special_positions)
