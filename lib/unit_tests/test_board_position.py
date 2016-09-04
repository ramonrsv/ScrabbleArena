import unittest
from ..board_position import PosProperty, Position


class TestPosProperty(unittest.TestCase):
    def test_simple_isinstance(self):
        self.assertIsInstance(PosProperty.normal, PosProperty)
        self.assertIsInstance(PosProperty.CENTER, PosProperty)
        self.assertIsInstance(PosProperty.DW, PosProperty)
        self.assertIsInstance(PosProperty.W3, PosProperty)

    def test_equal_enums(self):
        self.assertEqual(PosProperty.L2, PosProperty.DL)
        self.assertEqual(PosProperty.L3, PosProperty.TL)
        self.assertEqual(PosProperty.W2, PosProperty.DW)
        self.assertEqual(PosProperty.W3, PosProperty.TW)

    def test_bool_op(self):
        self.assertFalse(True if PosProperty.normal.value else False)
        self.assertTrue(True if PosProperty.CENTER.value else False)
        self.assertFalse(bool(PosProperty.normal.value))
        self.assertTrue(bool(PosProperty.CENTER.value))

    def test_letter_multiplier(self):
        self.assertEqual(PosProperty.letter_multiplier(PosProperty.normal), 1)
        self.assertEqual(PosProperty.letter_multiplier(PosProperty.DW), 1)
        self.assertEqual(PosProperty.letter_multiplier(PosProperty.L2), 2)
        self.assertEqual(PosProperty.letter_multiplier(PosProperty.L3), 3)

    def test_word_multiplier(self):
        self.assertEqual(PosProperty.word_multiplier(PosProperty.normal), 1)
        self.assertEqual(PosProperty.word_multiplier(PosProperty.DL), 1)
        self.assertEqual(PosProperty.word_multiplier(PosProperty.W2), 2)
        self.assertEqual(PosProperty.word_multiplier(PosProperty.W3), 3)
        self.assertEqual(PosProperty.word_multiplier(PosProperty.W4), 4)


class TestPosition(unittest.TestCase):
    def test_simple_construction(self):
        pos = Position(2, 10)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 10)

    def test_property_default(self):
        self.assertEqual(Position(1, 1).property, PosProperty.normal)

    def test_property_construction_and_setter(self):
        pos = Position(1, 1, PosProperty.CENTER)
        self.assertEqual(pos.property, PosProperty.CENTER)
        pos.property = PosProperty.DL
        self.assertEqual(pos.property, PosProperty.DL)


if __name__ == "__main__":
    unittest.main()
