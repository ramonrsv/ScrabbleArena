import string


class Dimension:
    def __init__(self, width, height):
        self._width = width  # Not required in __init__, but here to follow PEP
        self._height = height
        self.width = width
        self.height = height

    @staticmethod
    def _dimension_check(dim):
        if not isinstance(dim, int) or dim <= 0:
            raise TypeError("invalid value: " + str(dim) + " - not a positive integer")
        return dim

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, w):
        self._width = self._dimension_check(w)

    @height.setter
    def height(self, h):
        self._height = self._dimension_check(h)

    @staticmethod
    def center_coo(width, height):
        return (None if width % 2 == 0 else width // 2 + 1), (None if height % 2 == 0 else height // 2 + 1)

    @staticmethod
    def in_bounds(pos, bounds):
        """Takes position in (x,y) and bounds in {x:(1,2), y:(1,2)} form"""
        return bounds['x'][0] <= pos[0] <= bounds['x'][1] and bounds['y'][0] <= pos[1] <= bounds['y'][1]


class Coordinate:
    def __init__(self, x, y):
        self._x = x  # Not required, but here to follow PEP
        self._y = y
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    @staticmethod
    def x_to_alpha(x):
        if not isinstance(x, int) or x <= 0:
            raise TypeError("invalid value: '" + str(x) + "' - is not a positive integer")
        if x > len(string.ascii_uppercase):
            raise ValueError("invalid value: '" + str(x) + "' - is greater than ascii_lowercase/uppercase")
        return string.ascii_uppercase[x - 1]

    @staticmethod
    def alpha_to_x(alpha):
        if alpha not in string.ascii_letters:
            raise TypeError("invalid value: '" + str(alpha) + "' - not in ascii_letters")
        return string.ascii_uppercase.index(alpha.upper()) + 1

    @property
    def x(self):
        return self._x

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
            self._x = x

    @x_alpha.setter
    def x_alpha(self, xa):
        try:
            self.x = self.alpha_to_x(xa)
        except (TypeError, ValueError):
            raise

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if not isinstance(y, int) or y <= 0:
            raise TypeError("invalid value: '" + str(y) + "' - is not a positive integer")
        self._y = y

    @property
    def coo(self):
        return self.x, self.y

    @property
    def coo_alpha(self):
        return self.x_alpha, self.y
