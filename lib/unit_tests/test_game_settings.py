import unittest
import string
from lib.letter_value_map import LetterValueMap
from lib.game_settings.game_settings import GameSettings
from lib.game_settings.letter_value_maps import English_classic_lvm
from lib.game_settings.tile_bag_distributions import English_classic_100_tbd
from lib.game_settings.board_configurations import Words_with_friends_board_configuration


class TestGameSettings(unittest.TestCase):
    def test_bad_letter_value_map(self):
        self.assertRaises(AssertionError, lambda: GameSettings("bad", English_classic_100_tbd,
                                                               Words_with_friends_board_configuration, 10))

    def test_bad_tile_bag_distribution(self):
        self.assertRaises(AssertionError, lambda: GameSettings(English_classic_lvm, "bad",
                                                               Words_with_friends_board_configuration, 10))

    def test_bad_board_configuration(self):
        self.assertRaises(AssertionError, lambda: GameSettings(English_classic_lvm, English_classic_100_tbd,
                                                               "bad", 10))

    def test_bad_player_tray_size(self):
        self.assertRaises(AssertionError, lambda: GameSettings(English_classic_lvm, English_classic_100_tbd,
                                                               Words_with_friends_board_configuration, "bad"))
        self.assertRaises(AssertionError, lambda: GameSettings(English_classic_lvm, English_classic_100_tbd,
                                                               Words_with_friends_board_configuration, 0))
        self.assertRaises(AssertionError, lambda: GameSettings(English_classic_lvm, English_classic_100_tbd,
                                                               Words_with_friends_board_configuration, -1))

    def test_mismatched_letter_value_map_and_tile_bag_distributions(self):
        lvm = LetterValueMap({LetterValueMap.BLANK: 0, 'A': 1, 'B': 2, 'C': 3})
        self.assertRaises(AssertionError, lambda: GameSettings(lvm, English_classic_100_tbd,
                                                               Words_with_friends_board_configuration, 10))


class TestLetterValueMaps(unittest.TestCase):
    def test_english_classic_letters_are_alphabet(self):
        non_blank_letters = [letter for letter in English_classic_lvm.all_letters() if letter != LetterValueMap.BLANK]
        self.assertEqual(set(non_blank_letters), set(list(string.ascii_uppercase)))


class TestTileBagDistributions(unittest.TestCase):
    def test_english_classic_100_total_tiles(self):
        count = sum(
            [English_classic_100_tbd.get_letter_frequency(letter) for letter in English_classic_100_tbd.all_letters()])
        self.assertEqual(count, 100)


if __name__ == "__main__":
    unittest.main()
