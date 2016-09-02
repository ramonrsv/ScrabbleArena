import unittest
from tile import LetterError, Tile
from settings import English_classic_letter_distribution


class TestTile(unittest.TestCase):
    def setUp(self):
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

if __name__ == "__main__":
    unittest.main()
