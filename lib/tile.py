import copy
import time
import random


class LetterError(TypeError):
    pass


class Tile:
    """Interface class for Tiles. Specific Tiles (differ in language, letter distribution, etc.) inherit from it"""

    BLANK = None
    _letter_distribution = {None: 0}
    # TODO: The solution of having a globally set letter distribution for all Tiles is rather dirty
    # It has to be set before Tiles are used (see use in test_tile.py) and changing it after could be problematic
    # You also need to know what LetterDistribution a TileDistribution uses before creating a TileBag
    # The intended purpose was to have, say, EnglishTile defined with the given LetterDistribution set, but Tile
    # has been used directly everywhere - see how that affects things.

    def __init__(self, letter, blank=False):
        self.__blank = blank
        self.__letter = letter  # Not required, but here to follow PEP
        self.letter = letter

    @classmethod
    def blank_tile(cls, letter=None):
        """Permits the more intuitive initialization of a blank tile:
        tile = Tile.blank_tile('A') or tile = Tile.blank_tile(Tile.BLANK)"""
        return cls(letter if letter else cls.BLANK, blank=True)

    def isblank(self):
        return self.__blank

    @property
    def letter(self):
        return self.__letter

    @letter.setter
    def letter(self, letter):
        if letter not in self._letter_distribution:
            if letter.upper() in self._letter_distribution:
                raise LetterError(str(letter) +
                                  "is not a valid letter - 'letter_distribution' is generally only uppercase")
            raise LetterError(str(letter) + " is not a valid letter")
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


class TileBag:
    def __init__(self, tile_distribution):
        self._tile_distribution = tile_distribution
        self._tiles_left = copy.deepcopy(tile_distribution.tiles)
        random.seed(time.time())  # Used for random tile selection

    def remaining(self, letter=None):
        """Return the number of 'letter' remaining - all tiles if letter==None"""
        return self._tiles_left[letter] if letter else sum(n for key, n in self._tiles_left.items())

    def take(self, n):
        """Return n random tiles from the ones left in the bag"""
        if self.remaining() < n:
            raise ValueError("invalid value: " + str(n) + " - only " + str(self.remaining()) + " tiles left")
        tiles_to_return = []
        letters_available = [key for key, value in self._tiles_left.items() if value > 0]
        for i in range(n):
            rand_letter = letters_available[random.randrange(len(letters_available))]
            tiles_to_return.append(
                Tile(rand_letter, blank=True if rand_letter == self._tile_distribution.BLANK else False))
            self._tiles_left[rand_letter] -= 1
            if self._tiles_left[rand_letter] == 0:
                letters_available.remove(rand_letter)
        return tiles_to_return


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
        self.letter_distribution = letter_distribution
