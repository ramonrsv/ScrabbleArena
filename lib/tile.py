import abc


class LetterError(TypeError):
    pass


class Tile:
    """Interface class for Tiles. Specific Tiles (differ in language, letter distribution, etc.) inherit from it"""
    __metaclass__ = abc.ABCMeta

    BLANK = None
    _letter_distribution = {None: 0}

    def __init__(self, letter, blank=False):
        self.__blank = blank
        self.__letter = letter  # Not required, but here to follow PEP
        self.letter = letter

    @classmethod
    def blank_tile(cls, letter=BLANK):
        """Permits the more intuitive initialization of a blank tile:
        tile = Tile.blank_tile('A') or tile = Tile.blank_tile(Tile.BLANK)"""
        return cls(letter, blank=True)

    def isblank(self):
        return self.__blank

    def __bool__(self):
        return bool(self.letter)

    @property
    def letter(self):
        return self.__letter

    @letter.setter
    def letter(self, letter):
        if letter not in self._letter_distribution:
            if letter.upper() in self._letter_distribution:
                raise LetterError(str(letter) +
                                  "is not a valid letter - 'letter_distribution' is generally only uppercase")
            raise LetterError(str(letter) + "is not a valid letter")
        self.__letter = letter

    @property
    def value(self):
        if self.isblank():  # If tile is blank value is given by BLANK in letter_distribution, not by the current letter
            return self._letter_distribution[self.BLANK]
        return self._letter_distribution[self.letter]

    @classmethod
    def get_letter_distribution(cls):
        return cls._letter_distribution

    @classmethod
    def set_letter_distribution(cls, distribution):
        if not isinstance(distribution, LetterDistribution):
            raise TypeError("distribution has to be a LetterDistribution")
        cls.BLANK = distribution.BLANK
        cls._letter_distribution = distribution.letters


class LetterDistribution:
    """Contains a map of all Letters and their respective values"""
    def __init__(self, blank, distribution):
        self.BLANK = blank
        self.letters = distribution
        if not isinstance(distribution, dict):
            raise TypeError("distribution has to be a dictionary")
        if self.BLANK not in distribution:
            raise ValueError("BLANK has to be in distribution")


class TileDistribution:
    """Contains a map of all Letters in a LetterDistribution with their respective frequency"""
    def __init__(self, letter_distribution, tile_distribution):
        if not isinstance(letter_distribution, LetterDistribution):
            raise TypeError("letter_distribution has to be a LetterDistribution")
        if not isinstance(tile_distribution, dict):
            raise TypeError("tile_distribution has to be a dictionary")
        if set(letter_distribution.letters.keys()) != set(tile_distribution.keys()):
            raise ValueError("tile_distribution has to have an entry for every letter in letter_distribution")
        self.BLANK = letter_distribution.BLANK
        self.tiles = tile_distribution
