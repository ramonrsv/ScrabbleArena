import unittest
from ..settings import English_classic_letter_distribution, English_classic_100_tile_distribution
import string


class TestDistributions(unittest.TestCase):
    def test_letters_are_alphabet(self):
        no_blank_letters = [letter for letter in English_classic_letter_distribution.letters.keys()
                            if letter is not English_classic_letter_distribution.BLANK]
        self.assertEqual(set(no_blank_letters), set(list(string.ascii_uppercase)))

    def test_total_tiles(self):
        count = 0
        for key, value in English_classic_100_tile_distribution.tiles.items():
            count += value
        self.assertEqual(count, 100)


if __name__ == "__main__":
    unittest.main()
