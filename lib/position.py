from enum import Enum
from abc import ABCMeta, abstractmethod
from .dimension_and_coordinate import Coordinate


class PositionProperty(Enum):
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


class Position(Coordinate):
    def __init__(self, x, y, pos_property):
        Coordinate.__init__(self, x, y)
        self.__property = pos_property
        self.property = pos_property

    @property
    def property(self):
        return self.__property

    @property.setter
    def property(self, pos_property):
        if not isinstance(pos_property, PositionProperty):
            raise TypeError("invalid type: " + str(type(pos_property)) + " - is not " + str(type(PositionProperty)))
        self.__property = pos_property


class ClassicPositionProperty(PositionProperty):
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
