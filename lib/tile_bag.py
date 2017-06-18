import copy
import time
import random
from lib.letter_value_map import LetterValueMap


class Tile:
    DEFAULT_BLANK_LETTER = " "

    def __init__(self, letter, isblank=False, tile_bag=None):
        # If a reference to a tile_bag is provided some functionality in a TileBag can be accessed directly through the
        # Tile (get_letter_value, get_letter_frequency, etc.), as well as additional error checking.
        self._isblank = isblank  # Blank tiles can change their letter but we need to remember that they are Blank
        if tile_bag is not None:
            assert isinstance(tile_bag, TileBag), "tile_bag must be of type TileBag"
        self._tile_bag = tile_bag

        if self.has_bag():
            assert self._is_letter_valid(letter), "letter " + str(letter) + "is invalid"
        self._letter = letter

    @classmethod
    def blank_tile(cls, letter=None, tile_bag=None):
        """Permits a more intuitive initialization of a blank tile:
        tile = Tile.blank_tile(), tile = Tile.blank_tile('A'), or tile = Tile.blank_tile(BLANK)"""
        return cls(letter if letter is not None else cls.DEFAULT_BLANK_LETTER, isblank=True, tile_bag=tile_bag)

    def is_blank(self):
        return self._isblank

    def has_bag(self):
        return True if self._tile_bag is not None else False

    def _assert_has_bag(self):
        if not self.has_bag():
            raise RuntimeError("this instance of Tile does not have a tile_bag reference")

    @property
    def letter(self):
        return self._letter

    @letter.setter
    def letter(self, letter):
        if not self.is_blank():
            raise RuntimeError("Cannot modify letter of a non-blank tile")
        if self.has_bag() and not self._is_letter_valid(letter):
            raise ValueError(str(letter) + " is not a valid letter")
        self._letter = letter

    def bag(self):
        self._assert_has_bag()
        return self._tile_bag

    def _is_letter_valid(self, letter):
        self._assert_has_bag()
        if letter == self.bag().BLANK and not self.is_blank():
            return False
        else:
            return self.bag().is_letter_valid(letter)

    @property
    def value(self):
        self._assert_has_bag()
        return self.bag().get_letter_value(self.letter)

    @property
    def frequency(self):
        self._assert_has_bag()
        return self.bag().get_letter_frequency(self.letter)


class TileBagDistribution(LetterValueMap):
    """Contains a map of all the Letters in a LetterValueMap with their respective frequencies in tiles"""
    # TODO: Review design decision to inherit from LetterValueMap
    # The information in the LetterValueMap is used in a couple of levels up.
    # To solve this issue TileBag inherits from TileBagDistribution, which inherits from LetterValueMap
    # TileBag and TileBagDistribution contain a init_params() method that returns the methods they were initialized
    # with so that a copy-construction can be made.

    def __init__(self, letter_value_map, letter_frequency_dict):
        assert isinstance(letter_value_map, LetterValueMap), "letter_value_map must be of type LetterValueMap"

        LetterValueMap.__init__(self, LetterValueMap.init_params(letter_value_map))

        self._validate_letter_frequency_dict(letter_value_map, letter_frequency_dict)
        self._letter_frequency_dict = letter_frequency_dict

    @staticmethod
    def _validate_letter_frequency_dict(letter_value_map, letter_frequency_dict):
        assert isinstance(letter_frequency_dict, dict), "letter_frequency_dict must be dict type"
        assert sorted(letter_value_map.all_letters()) == sorted(letter_frequency_dict.keys()), \
            "all letters in letter_value_map must have a frequency in letter_frequency_dict"
        for letter, freq in letter_frequency_dict.items():
            assert isinstance(freq, int) and freq >= 0, "frequency must be a positive integer"

    def get_letter_frequency(self, letter):
        return self._letter_frequency_dict[letter]

    # TODO: This is to support a dirty copy-construction. Find a more pythonic way to do this.
    def init_params(self):
        return self, self._letter_frequency_dict


class TileBag(TileBagDistribution):
    def __init__(self, tile_bag_distribution):
        assert isinstance(tile_bag_distribution, TileBagDistribution), \
            "tile_bag_distribution must be of type TileBagDistribution"

        TileBagDistribution.__init__(self, *TileBagDistribution.init_params(tile_bag_distribution))

        self._tiles_left = copy.deepcopy(self._letter_frequency_dict)
        random.seed(time.time())  # Used for random tile selection

    def remaining(self, letter=None):
        """Return the number of 'letter' remaining - all tiles if letter==None"""
        return self._tiles_left[letter] if letter is not None else sum(n for key, n in self._tiles_left.items())

    def take(self, letter=None):
        """Return ONE random Tile, or of letter if specified"""
        return self.take_multiple(1, letter)[0]

    def take_multiple(self, n, letter=None):
        """Return a list of n Tiles. Random if letter is None, else all of letter"""
        assert self.remaining() >= n, "invalid value: " + str(n) + " - only " + str(self.remaining()) + " tiles left"

        if letter is not None:
            return self._take_specific(n, letter)
        else:
            return self._take_random(n)

    def _take_specific(self, n, letter):
        """Return a list of n Tiles of letter"""
        assert self.remaining(letter) >= n, \
            "invalid value: " + str(n) + " - only " + str(self.remaining(letter)) + " tiles of '" + letter + "' left"

        self._tiles_left[letter] -= n
        return [self._factory_make_tile(letter, is_blank=True if letter == self.BLANK else False, tile_bag=self)
                for _ in range(n)]

    def _take_random(self, n):
        """Return a list of n random Tiles"""
        tiles_to_return = []
        letters_available = [key for key in self._tiles_left if self.remaining(key) > 0]
        for i in range(n):
            rand_letter = letters_available[random.randrange(len(letters_available))]
            tiles_to_return.extend(self._take_specific(1, rand_letter))
            if self.remaining(rand_letter) == 0:
                letters_available.remove(rand_letter)
        return tiles_to_return

    def put_back(self, tile):
        """Return a Tile to the TileBag"""
        assert isinstance(tile, Tile), "tile must be of type Tile"
        assert self.remaining(tile.letter) < self.get_letter_frequency(tile.letter), \
            "number of remaining tiles cannot exceed original frequency - (letter, remaining, freq) == " + \
            "(" + tile.letter + ", " + self.remaining(tile.letter) + ", " + self.get_letter_frequency(tile.letter) + ")"
        self._tiles_left[tile.letter] += 1

    def put_back_multiple(self, tiles):
        """Return a list of Tiles to the TileBag"""
        for tile in tiles:
            self.put_back(tile)

    @classmethod
    def _factory_make_tile(cls, letter, is_blank, tile_bag):
        return Tile(letter, is_blank, tile_bag)
