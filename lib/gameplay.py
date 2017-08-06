from .position import Position, ClassicPositionAttribute as PosAttribute
from .board import Board
from .tile_bag import Tile


class PlayError(RuntimeError):
    pass


class GameplayPosition(Position):
    def __init__(self, x, y, pos_attribute=PosAttribute.normal):
        Position.__init__(self, x, y, pos_attribute)


class GameplayBoard(Board):
    def __init__(self, board_configuration):
        Board.__init__(self, board_configuration)

    def _factory_make_position(self, position):
        """Overloading Board definition to return GameplayPosition instead"""
        return GameplayPosition(position.x, position.y, position.attribute)


class TileTray:
    def __init__(self, tiles, size):
        if len(tiles) > size:
            raise ValueError("more tiles than size of tray: " + str(len(tiles)) + " tiles and size " + str(size))
        self._size = size
        self._tiles = tiles

    @property
    def size(self):
        return self._size

    @property
    def tiles(self):
        return self._tiles

    def remove(self, tile):
        if tile not in self.tiles:
            raise RuntimeError("tile not found in list")
        self.tiles.remove(tile)
        return tile

    def left(self):
        return len(self.tiles)
