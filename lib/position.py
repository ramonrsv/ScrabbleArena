from enum import Enum
from abc import ABCMeta, abstractmethod
from lib.dimension_and_coordinate import Coordinate
from lib.tile_bag import Tile


class PositionAttribute(Enum):
    """This is an Interface class. Any subclass must define all the 'Enums' and the abstract methods"""
    __metaclass__ = ABCMeta

    @classmethod
    @abstractmethod
    def _letter_multiplier_dict(cls):
        # Because 'Enums' not defined in partial_dict (in _create_full_multiplier_dict) are given the 'default_value',
        # errors in partial_dict may go undetected. However, forcing the user to define value for all 'Enums' would be
        # error prone and not offer any more error checking functionality.
        pass  # Define as return cls._get_full_letter_multiplier_dict({?}, default_value=?)

    @classmethod
    @abstractmethod
    def _word_multiplier_dict(cls):
        pass  # Define as return cls._get_full_word_multiplier_dict({?}, default_value=?)

    def letter_multiplier(self):
        return self.get_letter_multiplier(self)

    def word_multiplier(self):
        return self.get_word_multiplier(self)

    @classmethod
    def get_letter_multiplier(cls, enum):
        if not isinstance(enum, Enum):
            raise TypeError("invalid type: " + str(type(enum)) + " must have " + str(type(cls)) + " type")
        return cls._letter_multiplier_dict()[enum]

    @classmethod
    def get_word_multiplier(cls, enum):
        if not isinstance(enum, Enum):
            raise TypeError("invalid type: " + str(type(enum)) + " must have " + str(type(cls)) + " type")
        return cls._word_multiplier_dict()[enum]

    @classmethod
    def _get_full_letter_multiplier_dict(cls, partial_dict, default_value):
        return getattr(cls, "full_letter_dict", cls._create_full_multiplier_dict(partial_dict, default_value))

    @classmethod
    def _get_full_word_multiplier_dict(cls, partial_dict, default_value):
        return getattr(cls, "full_word_dict", cls._create_full_multiplier_dict(partial_dict, default_value))

    @classmethod
    def _create_full_multiplier_dict(cls, partial_dict, default_value):
        ret = dict()
        for enum in cls:
            ret[enum] = partial_dict.get(enum, default_value)
        return ret


class ClassicPositionAttribute(PositionAttribute):
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


class Position(Coordinate):
    def __init__(self, x, y, pos_attribute=ClassicPositionAttribute.normal):
        Coordinate.__init__(self, x, y)
        self._attribute = pos_attribute
        self.attribute = pos_attribute
        self._tile = None

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, pos_attribute):
        if not isinstance(pos_attribute, PositionAttribute):
            raise TypeError("invalid type: " + str(type(pos_attribute)) + " - is not " + str(type(PositionAttribute)))
        self._attribute = pos_attribute

    def has_tile(self):
        return True if self._tile is not None else False

    def get_tile(self):
        if not self.has_tile():
            raise RuntimeError("position does not currently have a tile")
        return self._tile

    def set_tile(self, tile):
        if not isinstance(tile, Tile):
            raise TypeError("tile has to be a Tile object")
        if self._tile is not None:
            raise RuntimeError("position already has a tile object")
        self._tile = tile

    def remove_tile(self):
        if not self.has_tile():
            raise RuntimeError("position does not currently have a tile")
        self._tile = None

    @property
    def tile(self):
        return self.get_tile()

    @tile.setter
    def tile(self, tile):
        self.set_tile(tile)
