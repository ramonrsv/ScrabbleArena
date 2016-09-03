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

    def test_coo_to_alpha(self):
        self.assertEqual(Position.coo_to_alpha(1), 'A')
        self.assertEqual(Position.coo_to_alpha(26), 'Z')

    def test_alpha_to_coo(self):
        self.assertEqual(Position.alpha_to_coo('A'), 1)
        self.assertEqual(Position.alpha_to_coo('a'), 1)
        self.assertEqual(Position.alpha_to_coo('Z'), 26)
        self.assertEqual(Position.alpha_to_coo('z'), 26)

    def test_coo_to_alpha_type_error(self):
        self.assertRaises(TypeError, lambda: Position.coo_to_alpha('A'))

    def test_coo_to_alpha_value_error(self):
        self.assertRaises(ValueError, lambda: Position.coo_to_alpha(27))

    def test_alpha_to_coo_type_error(self):
        self.assertRaises(TypeError, lambda: Position.alpha_to_coo('\n'))
        self.assertRaises(TypeError, lambda: Position.alpha_to_coo(1))

    def test_alpha_construction(self):
        pos = Position('A', 3)
        self.assertEqual(pos.x, 1)
        self.assertEqual(pos.y, 3)

    def test_alpha_property(self):
        pos = Position('B', 10)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.x_alpha, 'B')
        self.assertEqual(pos.y, 10)

    def test_alpha_setter(self):
        pos = Position(1, 1)
        self.assertEqual(pos.x, 1)
        self.assertEqual(pos.y, 1)
        pos.x = 'B'
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.x_alpha, 'B')
        pos.x_alpha = 'C'
        self.assertEqual(pos.x, 3)
        self.assertEqual(pos.x_alpha, 'C')

    def test_coo(self):
        self.assertEqual(Position(1, 1).coo, (1, 1))
        self.assertEqual(Position('Z', 10).coo, (26, 10))

    def test_property_default(self):
        self.assertEqual(Position(1, 1).property, PosProperty.normal)

    def test_property_construction_and_setter(self):
        pos = Position(1, 1, PosProperty.CENTER)
        self.assertEqual(pos.property, PosProperty.CENTER)
        pos.property = PosProperty.DL
        self.assertEqual(pos.property, PosProperty.DL)

if __name__ == "__main__":
    unittest.main()
