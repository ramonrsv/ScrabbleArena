from enum import Enum
import string


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
        return {PosProperty.L2: 2, PosProperty.L3: 3}, {PosProperty.W2: 2, PosProperty.W3: 3, PosProperty.W4: 4}

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


class Position:
    def __init__(self, x, y, pos_property=PosProperty.normal):
        self.__x = x  # Not required, but here to follow PEP
        self.__y = y
        self.__property = pos_property
        self.x = x
        self.y = y
        self.property = pos_property

    @staticmethod
    def coo_to_alpha(coo):
        if not isinstance(coo, int) or coo <= 0:
            raise TypeError("invalid value: '" + str(coo) + "' - is not a positive integer")
        if coo > len(string.ascii_uppercase):
            raise ValueError("invalid value: '" + str(coo) + "' - is greater than ascii_lowercase/uppercase")
        return string.ascii_uppercase[coo - 1]

    @staticmethod
    def alpha_to_coo(alpha):
        if alpha not in string.ascii_letters:
            raise TypeError("invalid value: '" + str(alpha) + "' - not in ascii_letters")
        return string.ascii_uppercase.index(alpha.upper()) + 1

    @property
    def x(self):
        return self.__x

    @property
    def x_alpha(self):
        return self.coo_to_alpha(self.x)

    @x.setter
    def x(self, x):
        if isinstance(x, str):  # Allow alpha setting on x and constructor
            self.x_alpha = x
        else:
            if not isinstance(x, int) or x <= 0:
                raise TypeError("invalid value: '" + str(x) + "' - is not a positive integer")
            self.__x = x

    @x_alpha.setter
    def x_alpha(self, xa):
        try:
            self.x = self.alpha_to_coo(xa)
        except (TypeError, ValueError):
            raise

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int) or y <= 0:
            raise TypeError("invalid value: '" + str(y) + "' - is not a positive integer")
        self.__y = y

    @property
    def coo(self):
        return self.x, self.y

    @property
    def property(self):
        return self.__property

    @property.setter
    def property(self, pos_property):
        if not isinstance(pos_property, type(PosProperty.normal)):
            raise TypeError("invalid type: " + str(type(pos_property)) + " - is not " + str(type(PosProperty.normal)))
        self.__property = pos_property
