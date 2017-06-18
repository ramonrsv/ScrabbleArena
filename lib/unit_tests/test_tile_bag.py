import unittest
import random
from lib.letter_value_map import LetterValueMap
from lib.tile_bag import Tile, TileBagDistribution, TileBag


class TestTileBagDistribution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_lvm = LetterValueMap({LetterValueMap.BLANK: 0, 'A': 1, 'B': 3, 'C': 3})

    def setUp(self):
        self.tbd = TileBagDistribution(self.sample_lvm, {LetterValueMap.BLANK: 0, 'A': 1, 'B': 2, 'C': 3})

    def test_correct_construction(self):
        try:
            TileBagDistribution(self.sample_lvm, {LetterValueMap.BLANK: 5, 'A': 5, 'B': 5, 'C': 5})
        except AssertionError:
            self.fail("construction with matching LetterValueMap should not fail")

    def test_construction_with_non_matching_letter_value_map(self):
        self.assertRaises(AssertionError,
                          lambda: TileBagDistribution(self.sample_lvm, {LetterValueMap.BLANK: 5, 'A': 5}))

    def test_construction_with_negative_frequency(self):
        self.assertRaises(AssertionError, lambda: TileBagDistribution(
            self.sample_lvm, {LetterValueMap.BLANK: 5, 'A': 5, 'B': 5, 'C': -1}))

    def test_get_letter_frequency(self):
        keys = [LetterValueMap.BLANK, 'A', 'B', 'C']
        for letter in keys:
            self.assertEqual(self.tbd.get_letter_frequency(letter), keys.index(letter))

    def test_get_letter_frequency_with_invalid_letter(self):
        self.assertRaises(KeyError, lambda: self.tbd.get_letter_frequency('Z'))

    def test_letter_value_map_interface_is_present(self):
        methods = ['get_letter_value', 'is_letter_valid', 'all_letters']
        for method in methods:
            if not hasattr(self.tbd, method):
                self.fail("TileBagDistribution does not have method '" + method + "'")
        self.assertEqual(self.tbd.get_letter_value('A'), 1)
        self.assertTrue(self.tbd.is_letter_valid('A'))
        self.assertFalse(self.tbd.is_letter_valid('Z'))


class TestTileBag(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample_lvm = LetterValueMap({LetterValueMap.BLANK: 0, 'A': 1, 'B': 3, 'C': 3})
        cls.sample_tbd = TileBagDistribution(cls.sample_lvm, {LetterValueMap.BLANK: 4, 'A': 1, 'B': 2, 'C': 3})

    def setUp(self):
        try:
            self.tile_bag = TileBag(self.sample_tbd)
        except AssertionError:
            self.fail("simple TileBag Construction with correct TileBagDistribution raised AssertionError")

    def test_correct_setup_construction(self):
        self.assertIsInstance(self.tile_bag, TileBag)

    def test_bad_argument_construction(self):
        self.assertRaises(AssertionError, lambda: TileBag("dummy variable"))

    def test_remaining_before_take(self):
        self.assertEqual(self.tile_bag.remaining(), 10)
        self.assertEqual(self.tile_bag.remaining(LetterValueMap.BLANK), 4)
        self.assertEqual(self.tile_bag.remaining('A'), 1)
        self.assertEqual(self.tile_bag.remaining('C'), 3)

    def test_remaining_with_invalid_letter(self):
        self.assertRaises(KeyError, lambda: self.tile_bag.remaining('Z'))

    def test_take_specific_letter(self):
        tile = self.tile_bag.take('A')
        self.assertIsInstance(tile, Tile)
        self.assertEqual(tile.letter, 'A')
        self.assertFalse(tile.is_blank())

    def test_take_blank_letter(self):
        tile = self.tile_bag.take(TileBag.BLANK)
        self.assertIsInstance(tile, Tile)
        self.assertTrue(tile.is_blank())
        self.assertEqual(tile.letter, TileBag.BLANK)

    def test_take_random(self):
        tile = self.tile_bag.take()
        self.assertIsInstance(tile, Tile)
        self.assertIn(tile.letter, self.sample_lvm.all_letters())

    def test_take_too_many(self):
        self.tile_bag.take('A')
        self.assertRaises(AssertionError, lambda: self.tile_bag.take('A'))

    def test_take_multiple_specific_letter(self):
        tiles = self.tile_bag.take_multiple(4, LetterValueMap.BLANK)
        self.assertIsInstance(tiles, list)
        self.assertEqual(len(tiles), 4)
        for tile in tiles:
            self.assertIsInstance(tile, Tile)
            self.assertEqual(tile.letter, TileBag.BLANK)
        tiles = self.tile_bag.take_multiple(1, 'A')
        self.assertEqual(len(tiles), 1)

    def test_take_multiple_random(self):
        tiles = self.tile_bag.take_multiple(10)
        for tile in tiles:
            self.assertIsInstance(tile, Tile)
            self.assertIn(tile.letter, self.sample_lvm.all_letters())

    def test_take_multiple_too_many(self):
        self.assertRaises(AssertionError, lambda: self.tile_bag.take_multiple(2, 'A'))
        self.assertRaises(AssertionError, lambda: self.tile_bag.take_multiple(11))

    def test_remaining_after_take(self):
        self.assertEqual(self.tile_bag.remaining(), 10)
        self.assertEqual(self.tile_bag.remaining('A'), 1)
        self.tile_bag.take('A')
        self.assertEqual(self.tile_bag.remaining('A'), 0)
        self.assertEqual(self.tile_bag.remaining(), 9)
        for _ in range(9):
            self.tile_bag.take()
        self.assertEqual(self.tile_bag.remaining(), 0)

    def test_put_back(self):
        self.assertEqual(self.tile_bag.remaining(), 10)
        self.assertEqual(self.tile_bag.remaining('A'), 1)
        tile = self.tile_bag.take('A')
        self.assertEqual(self.tile_bag.remaining(), 9)
        self.assertEqual(self.tile_bag.remaining('A'), 0)
        self.tile_bag.put_back(tile)
        self.assertEqual(self.tile_bag.remaining(), 10)
        self.assertEqual(self.tile_bag.remaining('A'), 1)

    def test_put_back_multiple(self):
        self.assertEqual(self.tile_bag.remaining(), 10)
        self.assertEqual(self.tile_bag.remaining('C'), 3)
        tiles = self.tile_bag.take_multiple(3, 'C')
        self.assertEqual(self.tile_bag.remaining(), 7)
        self.assertEqual(self.tile_bag.remaining('C'), 0)
        self.tile_bag.put_back_multiple(tiles)
        self.assertEqual(self.tile_bag.remaining(), 10)
        self.assertEqual(self.tile_bag.remaining('C'), 3)

    def test_random_take_multiple_remaining_total_count(self):
        self.assertEqual(self.tile_bag.remaining(), 10)
        rem = self.tile_bag.remaining()
        while self.tile_bag.remaining() > 0:
            rand_take = random.randrange(1, self.tile_bag.remaining() + 1)
            self.assertEqual(len(self.tile_bag.take_multiple(rand_take)), rand_take)
            self.assertEqual(self.tile_bag.remaining(), rem - rand_take)
            rem -= rand_take


# class TestTile(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.sample_lvm = LetterValueMap({LetterValueMap.BLANK: 0, 'A': 1, 'B': 3, 'C': 3})
#         cls.sample_tbd = TileBagDistribution(cls.sample_lvm, {LetterValueMap.BLANK: 4, 'A': 1, 'B': 2, 'C': 3})
#         cls.sample_tb = TileBag(cls.sample_tbd)
#
#     def test_simple_construction(self):
#         ta = Tile('A')
#         tz = Tile('Z')
#         self.assertEqual(ta.letter, 'A')
#         self.assertEqual(tz.letter, 'Z')
#         self.assertEqual(ta.value, 1)
#         self.assertEqual(tz.value, 10)
#         self.assertFalse(ta.is_blank())
#         self.assertFalse(tz.is_blank())
#
#     def test_simple_letter_reassignment(self):
#         t = Tile('A')
#         self.assertEqual(t.letter, 'A')
#         self.assertEqual(t.value, 1)
#         t.letter = 'B'
#         self.assertEqual(t.letter, 'B')
#         self.assertEqual(t.value, 3)
#
#     def test_blank_tile_default_letter(self):
#         bt = Tile.blank_tile()
#         self.assertTrue(bt.isblank())
#         self.assertEqual(bt.letter, Tile.BLANK)
#         self.assertEqual(bt.value, 0)
#
#     def test_blank_tile_other_letter(self):
#         bt = Tile.blank_tile('A')
#         self.assertTrue(bt.isblank())
#         self.assertEqual(bt.letter, 'A')
#         self.assertEqual(bt.value, 0)
#
#     def test_blank_tile_letter_change(self):
#         bt = Tile.blank_tile('A')
#         self.assertTrue(bt.isblank())
#         self.assertEqual(bt.letter, 'A')
#         self.assertEqual(bt.value, 0)
#         bt.letter = 'B'
#         self.assertTrue(bt.isblank())
#         self.assertEqual(bt.letter, 'B')
#         self.assertEqual(bt.value, 0)
#         bt.letter = Tile.BLANK
#         self.assertTrue(bt.isblank())
#         self.assertEqual(bt.letter, Tile.BLANK)
#         self.assertEqual(bt.value, 0)
#
#     def test_get_letter_distribution(self):
#         self.assertEqual(Tile.get_letter_distribution(), English_classic_letter_distribution.letters)


if __name__ == "__main__":
    unittest.main()
