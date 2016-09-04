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
    def _quadrant_bounds(width, height, inclusive=False):
        """Return map of map of coordinate pair tuples for the bounds of all 4 quadrants in order.
        If inclusive and odd width/height, the center x/y coordinate is included in both ranges.
        For 4x4 it'd be {
            1: {'x': (3, 4), 'y': (1, 2)},
            2: {'x': (1, 2), 'y': (1, 2)},
            3: {'x': (1, 2), 'y': (3, 4)},
            4: {'x': (3, 4), 'y': (3, 4)}})"""
        near_range = lambda length, center: (1, length // 2 + (1 if center and inclusive else 0))
        far_range = lambda length, center: (length - (length // 2 - 1) - (1 if center and inclusive else 0), length)
        cx, cy = BoardConfiguration.center_coo(width, height)
        return {
            1: {'x': far_range(width, cx), 'y': near_range(height, cy)},
            2: {'x': near_range(width, cx), 'y': near_range(height, cy)},
            3: {'x': near_range(width, cx), 'y': far_range(height, cy)},
            4: {'x': far_range(width, cx), 'y': far_range(height, cy)}}

    @staticmethod
    def _find_quadrant(pos, width, height):
        quadrant_bounds = BoardConfiguration._quadrant_bounds(width, height)
        for key, value in quadrant_bounds.items():
            if BoardConfiguration.in_bounds(pos.coo, value):
                return key
        return None

    @staticmethod
    def _mirror_position(pos, direction, width, height):
        assert direction in ['x', 'y'], "bad direction '" + str(direction) + "'"  # TODO: Implement diagonal direction
        ret = Position(width - pos.x + 1 if direction == 'x' else pos.x,
                       height - pos.y + 1 if direction == 'y' else pos.y, pos.property)
        return ret if ret != pos else None

    @classmethod
    def from_corners_symmetry(cls, width, height, special_positions):
        """Only one corner has to be defined - common row/column has to be defined for odd width/height"""
        config = cls(width, height, special_positions)  # Does error checking on parameters
        if len(special_positions) == 0:
            return config

        quadrant = next((cls._find_quadrant(pos, width, height)  # Quadrant of first non center position
                        for pos in special_positions if cls._find_quadrant(pos, width, height)), None)

        if quadrant:  # if not quadrant all special positions are in odd column/rows
            quadrant_bounds = cls._quadrant_bounds(width, height, inclusive=True)[quadrant]
            for pos in special_positions:
                if not cls.in_bounds(pos.coo, quadrant_bounds):
                    raise ValueError("invalid position: " + str(pos.coo) + " - all positions must be in one corner")

        # _mirror_position return None if it can't be mirrored, ensure it is not appended to the list
        special_positions += [pos for pos in
                              [cls._mirror_position(pos, 'x', width, height) for pos in special_positions]
                              if pos]
        special_positions += [pos for pos in
                              [cls._mirror_position(pos, 'y', width, height) for pos in special_positions]
                              if pos]
        return BoardConfiguration(width, height, special_positions)
