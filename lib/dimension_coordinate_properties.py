import string


class DimensionProperty:
    def __init__(self, width, height):
        self.__width = width  # Not required in __init__, but here to follow PEP
        self.__height = height
        self.width = width
        self.height = height

    @staticmethod
    def _dimension_check(dim):
        if not isinstance(dim, int) or dim <= 0:
            raise TypeError("invalid value: " + str(dim) + " - not a positive integer")
        return dim

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, w):
        self.__width = self._dimension_check(w)

    @height.setter
    def height(self, h):
        self.__height = self._dimension_check(h)


class CoordinateProperty:
    def __init__(self, x, y):
        self.__x = x  # Not required, but here to follow PEP
        self.__y = y
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    @staticmethod
    def x_to_alpha(coo):
        if not isinstance(coo, int) or coo <= 0:
            raise TypeError("invalid value: '" + str(coo) + "' - is not a positive integer")
        if coo > len(string.ascii_uppercase):
            raise ValueError("invalid value: '" + str(coo) + "' - is greater than ascii_lowercase/uppercase")
        return string.ascii_uppercase[coo - 1]

    @staticmethod
    def alpha_to_x(alpha):
        if alpha not in string.ascii_letters:
            raise TypeError("invalid value: '" + str(alpha) + "' - not in ascii_letters")
        return string.ascii_uppercase.index(alpha.upper()) + 1

    @property
    def x(self):
        return self.__x

    @property
    def x_alpha(self):
        return self.x_to_alpha(self.x)

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
            self.x = self.alpha_to_x(xa)
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
    def coo_alpha(self):
        return self.x_alpha, self.y
