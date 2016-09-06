import unittest
import time
import random
from ..tile import LetterError, Tile, TileBag
from ..settings import English_classic_letter_distribution, English_classic_100_tile_distribution


class TestTile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Tile.set_letter_distribution(English_classic_letter_distribution)

    def test_simple_construction(self):
        ta = Tile('A')
        tz = Tile('Z')
        self.assertEqual(ta.letter, 'A')
        self.assertEqual(tz.letter, 'Z')
        self.assertEqual(ta.value, 1)
        self.assertEqual(tz.value, 10)
        self.assertFalse(ta.isblank())
        self.assertFalse(tz.isblank())

    def test_simple_letter_reassignment(self):
        t = Tile('A')
        self.assertEqual(t.letter, 'A')
        self.assertEqual(t.value, 1)
        t.letter = 'B'
        self.assertEqual(t.letter, 'B')
        self.assertEqual(t.value, 3)

    def test_bad_construction(self):
        self.assertRaises(LetterError, lambda: Tile('\n'))

    def test_bad_reassignment(self):
        ta = Tile('A')
        with self.assertRaises(LetterError):
            ta.letter = '\n'

    def test_blank_tile_default_letter(self):
        bt = Tile.blank_tile()
        self.assertTrue(bt.isblank())
        self.assertEqual(bt.letter, Tile.BLANK)
        self.assertEqual(bt.value, 0)

    def test_blank_tile_other_letter(self):
        bt = Tile.blank_tile('A')
        self.assertTrue(bt.isblank())
        self.assertEqual(bt.letter, 'A')
        self.assertEqual(bt.value, 0)

    def test_blank_tile_letter_change(self):
        bt = Tile.blank_tile('A')
        self.assertTrue(bt.isblank())
        self.assertEqual(bt.letter, 'A')
        self.assertEqual(bt.value, 0)
        bt.letter = 'B'
        self.assertTrue(bt.isblank())
        self.assertEqual(bt.letter, 'B')
        self.assertEqual(bt.value, 0)
        bt.letter = Tile.BLANK
        self.assertTrue(bt.isblank())
        self.assertEqual(bt.letter, Tile.BLANK)
        self.assertEqual(bt.value, 0)

    def test_get_letter_distribution(self):
        self.assertEqual(Tile.get_letter_distribution(), English_classic_letter_distribution.letters)


class TestTileBag(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Tile.set_letter_distribution(English_classic_letter_distribution)
        random.seed(time.time())

    def test_simple_construction_remaining(self):
        tb = TileBag(English_classic_100_tile_distribution)
        self.assertIsInstance(tb, TileBag)
        self.assertEqual(tb.remaining(), 100)
        for key in English_classic_100_tile_distribution.tiles:
            self.assertEqual(tb.remaining(key), English_classic_100_tile_distribution.tiles[key])

    def test_take(self):
        tb = TileBag(English_classic_100_tile_distribution)
        tile = tb.take(1)
        self.assertIsInstance(tile[0], Tile)

    def test_take_remaining_total_count(self):
        tb = TileBag(English_classic_100_tile_distribution)
        self.assertEqual(tb.remaining(), 100)
        self.assertEqual(len(tb.take(10)), 10)
        self.assertEqual(tb.remaining(), 90)
        rem = tb.remaining()
        while tb.remaining() > 0:
            rand_take = random.randrange(1, 11 if tb.remaining() > 10 else tb.remaining() + 1)
            self.assertEqual(len(tb.take(rand_take)), rand_take)
            self.assertEqual(tb.remaining(), rem - rand_take)
            rem -= rand_take

    def test_take_remaining_specific_count(self):
        tb = TileBag(English_classic_100_tile_distribution)
        tile = tb.take(1)
        self.assertEqual(tb.remaining(tile[0].letter), English_classic_100_tile_distribution.tiles[tile[0].letter] - 1)


if __name__ == "__main__":
    unittest.main()
