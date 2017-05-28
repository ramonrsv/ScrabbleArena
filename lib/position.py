from enum import Enum
from .dimension_and_coordinate import Coordinate


class PosProperty(Enum):
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

    @staticmethod
    def _get_letter_word_multiplier_dict():
        return {PosProperty.L2: 2,  # Letter multipliers
                PosProperty.L3: 3},\
               {PosProperty.W2: 2,  # Word multipliers
                PosProperty.W3: 3,
                PosProperty.W4: 4}

    @classmethod
    def letter_multiplier(cls, enum):
        if not isinstance(enum, type(cls.normal)):
            raise TypeError("invalid type: " + str(type(enum)) + " must have " + str(type(cls)) + " type")
        return cls._get_letter_word_multiplier_dict()[0].get(enum, 1)

    @classmethod
    def word_multiplier(cls, enum):
        if not isinstance(enum, type(cls.normal)):
            raise TypeError("invalid type: " + str(type(enum)) + " must have " + str(type(cls)) + " type")
        return cls._get_letter_word_multiplier_dict()[1].get(enum, 1)


class Position(Coordinate):
    def __init__(self, x, y, pos_property=PosProperty.normal):
        Coordinate.__init__(self, x, y)
        self.__property = pos_property
        self.property = pos_property

    @property
    def property(self):
        return self.__property

    @property.setter
    def property(self, pos_property):
        if not isinstance(pos_property, type(PosProperty.normal)):
            raise TypeError("invalid type: " + str(type(pos_property)) + " - is not " + str(type(PosProperty.normal)))
        self.__property = pos_property
