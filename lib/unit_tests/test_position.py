import unittest
from ..position import PositionProperty, Position
from ..settings import EnglishClassicPositionProperty


class TestPositionPropertyUsingEnglishClassic(unittest.TestCase):
    def test_simple_isinstance(self):
        self.assertIsInstance(EnglishClassicPositionProperty.normal, EnglishClassicPositionProperty)
        self.assertIsInstance(EnglishClassicPositionProperty.CENTER, EnglishClassicPositionProperty)
        self.assertIsInstance(EnglishClassicPositionProperty.DW, EnglishClassicPositionProperty)
        self.assertIsInstance(EnglishClassicPositionProperty.W3, EnglishClassicPositionProperty)

    def test_equal_enums(self):
        self.assertEqual(EnglishClassicPositionProperty.L2, EnglishClassicPositionProperty.DL)
        self.assertEqual(EnglishClassicPositionProperty.L3, EnglishClassicPositionProperty.TL)
        self.assertEqual(EnglishClassicPositionProperty.W2, EnglishClassicPositionProperty.DW)
        self.assertEqual(EnglishClassicPositionProperty.W3, EnglishClassicPositionProperty.TW)

    def test_bool_op(self):
        self.assertFalse(True if EnglishClassicPositionProperty.normal.value else False)
        self.assertTrue(True if EnglishClassicPositionProperty.CENTER.value else False)
        self.assertFalse(bool(EnglishClassicPositionProperty.normal.value))
        self.assertTrue(bool(EnglishClassicPositionProperty.CENTER.value))

    def test_class_letter_multiplier(self):
        self.assertEqual(EnglishClassicPositionProperty.get_letter_multiplier(EnglishClassicPositionProperty.normal), 1)
        self.assertEqual(EnglishClassicPositionProperty.get_letter_multiplier(EnglishClassicPositionProperty.DW), 1)
        self.assertEqual(EnglishClassicPositionProperty.get_letter_multiplier(EnglishClassicPositionProperty.L2), 2)
        self.assertEqual(EnglishClassicPositionProperty.get_letter_multiplier(EnglishClassicPositionProperty.L3), 3)

    def test_class_word_multiplier(self):
        self.assertEqual(EnglishClassicPositionProperty.get_word_multiplier(EnglishClassicPositionProperty.normal), 1)
        self.assertEqual(EnglishClassicPositionProperty.get_word_multiplier(EnglishClassicPositionProperty.DL), 1)
        self.assertEqual(EnglishClassicPositionProperty.get_word_multiplier(EnglishClassicPositionProperty.W2), 2)
        self.assertEqual(EnglishClassicPositionProperty.get_word_multiplier(EnglishClassicPositionProperty.W3), 3)
        self.assertEqual(EnglishClassicPositionProperty.get_word_multiplier(EnglishClassicPositionProperty.W4), 4)

    def test_object_letter_multiplier(self):
        self.assertEqual(EnglishClassicPositionProperty.normal.letter_multiplier(), 1)
        self.assertEqual(EnglishClassicPositionProperty.DW.letter_multiplier(), 1)
        self.assertEqual(EnglishClassicPositionProperty.L2.letter_multiplier(), 2)
        self.assertEqual(EnglishClassicPositionProperty.L3.letter_multiplier(), 3)

    def test_object_word_multiplier(self):
        self.assertEqual(EnglishClassicPositionProperty.normal.word_multiplier(), 1)
        self.assertEqual(EnglishClassicPositionProperty.DL.word_multiplier(), 1)
        self.assertEqual(EnglishClassicPositionProperty.W2.word_multiplier(), 2)
        self.assertEqual(EnglishClassicPositionProperty.W3.word_multiplier(), 3)
        self.assertEqual(EnglishClassicPositionProperty.W4.word_multiplier(), 4)


class TestNewPositionProperty(unittest.TestCase):
        class NewPositionProperty(PositionProperty):
            T1 = 0
            T2 = 1

            @classmethod
            def _letter_multiplier_dict(cls):
                return cls._get_full_letter_multiplier_dict({cls.T1: 1, cls.T2: 2}, default_value=1)

            @classmethod
            def _word_multiplier_dict(cls):
                return cls._get_full_word_multiplier_dict({cls.T1: 10}, default_value=1)

        def test_inherited_class_isinstance(self):
            self.assertIsInstance(self.NewPositionProperty.T1, self.NewPositionProperty)
            self.assertIsInstance(self.NewPositionProperty.T2, self.NewPositionProperty)

        def test_base_class_isinstance(self):
            self.assertIsInstance(self.NewPositionProperty.T1, PositionProperty)
            self.assertIsInstance(self.NewPositionProperty.T2, PositionProperty)

        def test_different_enum_property_multiplier(self):
            self.assertEqual(self.NewPositionProperty.get_word_multiplier(self.NewPositionProperty.T1), 10)
            self.assertEqual(self.NewPositionProperty.T1.letter_multiplier(), 1)


class TestPosition(unittest.TestCase):
    def test_simple_construction(self):
        pos = Position(2, 10, EnglishClassicPositionProperty.normal)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 10)

    def test_property_default(self):
        self.assertEqual(Position(1, 1, EnglishClassicPositionProperty.normal).property,
                         EnglishClassicPositionProperty.normal)

    def test_property_construction_and_setter(self):
        pos = Position(1, 1, EnglishClassicPositionProperty.CENTER)
        self.assertEqual(pos.property, EnglishClassicPositionProperty.CENTER)
        pos.property = EnglishClassicPositionProperty.DL
        self.assertEqual(pos.property, EnglishClassicPositionProperty.DL)


if __name__ == "__main__":
    unittest.main()
