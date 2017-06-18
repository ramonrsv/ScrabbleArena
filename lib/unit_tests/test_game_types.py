import unittest
import string
from lib.letter_value_map import LetterValueMap
from lib.game_types.letter_value_maps import English_classic_lvm
from lib.game_types.tile_bag_distributions import English_classic_100_tbd


class TestLetterValueMaps(unittest.TestCase):
    def test_english_classic_letters_are_alphabet(self):
        non_blank_letters = [letter for letter in English_classic_lvm.all_letters() if letter != LetterValueMap.BLANK]
        self.assertEqual(set(non_blank_letters), set(list(string.ascii_uppercase)))


class TestTileBagDistribution(unittest.TestCase):
    def test_english_classic_100_total_tiles(self):
        count = sum(
            [English_classic_100_tbd.get_letter_frequency(letter) for letter in English_classic_100_tbd.all_letters()])
        self.assertEqual(count, 100)


if __name__ == "__main__":
    unittest.main()
