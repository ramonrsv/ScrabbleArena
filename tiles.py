import abc


class LetterError(TypeError):
    pass


class AbstractTile:
    """Interface class for Tiles. Specific Tiles (differ in language, letter distribution, etc.) inherit from it"""
    __metaclass__ = abc.ABCMeta

    BLANK = None

    def __init__(self, letter, blank=False):
        self.__blank = blank
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
        if letter not in self.letter_distribution():
            if letter.upper() in self.letter_distribution():
                raise LetterError(str(letter) + "is in lowercase - 'letter_distribution' is generally only uppercase")
            raise LetterError(str(letter) + "is not a valid letter")
        self.__letter = letter

    @property
    def value(self):
        if self.isblank():  # If tile is blank value is given by BLANK in letter_distribution, not by the current letter
            return self.letter_distribution()[self.BLANK]
        return self.letter_distribution()[self.letter]

    @abc.abstractclassmethod
    def letter_distribution(cls):
        """Should return a dictionary of letter: value for all available letters of the given language. None is blank"""


class EnglishTile(AbstractTile):
    """Classic English alphabet and letter values"""
    @classmethod
    def letter_distribution(cls):
        return {cls.BLANK: 0,
                'A': 1,
                'B': 3,
                'C': 3,
                'D': 2,
                'E': 1,
                'F': 4,
                'G': 2,
                'H': 4,
                'I': 1,
                'J': 8,
                'M': 3,
                'N': 1,
                'O': 1,
                'P': 3,
                'Q': 10,
                'R': 1,
                'S': 1,
                'T': 1,
                'U': 1,
                'V': 4,
                'W': 4,
                'X': 8,
                'Y': 4,
                'Z': 10}
