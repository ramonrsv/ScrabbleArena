import unittest
from tiles import LetterError
from tiles import EnglishTile


class TestEnglishTile(unittest.TestCase):
    def test_simple_construction(self):
        ta = EnglishTile('A')
        tz = EnglishTile('Z')
        self.assertEqual(ta.letter, 'A')
        self.assertEqual(tz.letter, 'Z')
        self.assertEqual(ta.value, 1)
        self.assertEqual(tz.value, 10)
        self.assertFalse(ta.isblank())
        self.assertFalse(tz.isblank())

    def test_simple_letter_reassignment(self):
        t = EnglishTile('A')
        self.assertEqual(t.letter, 'A')
        self.assertEqual(t.value, 1)
        t.letter = 'B'
        self.assertEqual(t.letter, 'B')
        self.assertEqual(t.value, 3)

    def test_bad_construction(self):
        self.assertRaises(LetterError, lambda: EnglishTile('\n'))

    def test_bad_reassignment(self):
        ta = EnglishTile('A')
        with self.assertRaises(LetterError):
            ta.letter = '\n'

    def test_blank_tile_default_letter(self):
        bt = EnglishTile.blank_tile()
        self.assertTrue(bt.isblank())
        self.assertEqual(bt.letter, EnglishTile.BLANK)
        self.assertEqual(bt.value, 0)

    def test_blank_tile_other_letter(self):
        bt = EnglishTile.blank_tile('A')
        self.assertTrue(bt.isblank())
        self.assertEqual(bt.letter, 'A')
        self.assertEqual(bt.value, 0)

    def test_blank_tile_letter_change(self):
        bt = EnglishTile.blank_tile('A')
        self.assertTrue(bt.isblank())
        self.assertEqual(bt.letter, 'A')
        self.assertEqual(bt.value, 0)
        bt.letter = 'B'
        self.assertTrue(bt.isblank())
        self.assertEqual(bt.letter, 'B')
        self.assertEqual(bt.value, 0)
        bt.letter = EnglishTile.BLANK
        self.assertTrue(bt.isblank())
        self.assertEqual(bt.letter, EnglishTile.BLANK)
        self.assertEqual(bt.value, 0)


if __name__ == "__main__":
    unittest.main()