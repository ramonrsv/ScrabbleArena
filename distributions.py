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


English_letter_distribution = LetterDistribution(
    blank=None,
    distribution={
        None: 0,
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
        'K': 5,
        'L': 1,
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
        'Z': 10})

English_classic_100_tile_distribution = TileDistribution(
    letter_distribution=English_letter_distribution,
    tile_distribution={
        None: 2,
        'A': 9,
        'B': 2,
        'C': 2,
        'D': 4,
        'E': 12,
        'F': 2,
        'G': 3,
        'H': 2,
        'I': 9,
        'J': 1,
        'K': 1,
        'L': 4,
        'M': 2,
        'N': 6,
        'O': 8,
        'P': 2,
        'Q': 1,
        'R': 6,
        'S': 4,
        'T': 6,
        'U': 4,
        'V': 2,
        'W': 2,
        'X': 1,
        'Y': 2,
        'Z': 1})
