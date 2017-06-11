import unittest
from ..position import PositionProperty, Position
from lib.position import ClassicPositionProperty


class TestPositionPropertyUsingClassicPosition(unittest.TestCase):
    def test_simple_isinstance(self):
        self.assertIsInstance(ClassicPositionProperty.normal, ClassicPositionProperty)
        self.assertIsInstance(ClassicPositionProperty.CENTER, ClassicPositionProperty)
        self.assertIsInstance(ClassicPositionProperty.DW, ClassicPositionProperty)
        self.assertIsInstance(ClassicPositionProperty.W3, ClassicPositionProperty)

    def test_equal_enums(self):
        self.assertEqual(ClassicPositionProperty.L2, ClassicPositionProperty.DL)
        self.assertEqual(ClassicPositionProperty.L3, ClassicPositionProperty.TL)
        self.assertEqual(ClassicPositionProperty.W2, ClassicPositionProperty.DW)
        self.assertEqual(ClassicPositionProperty.W3, ClassicPositionProperty.TW)

    def test_bool_op(self):
        self.assertFalse(True if ClassicPositionProperty.normal.value else False)
        self.assertTrue(True if ClassicPositionProperty.CENTER.value else False)
        self.assertFalse(bool(ClassicPositionProperty.normal.value))
        self.assertTrue(bool(ClassicPositionProperty.CENTER.value))

    def test_class_letter_multiplier(self):
        self.assertEqual(ClassicPositionProperty.get_letter_multiplier(ClassicPositionProperty.normal), 1)
        self.assertEqual(ClassicPositionProperty.get_letter_multiplier(ClassicPositionProperty.DW), 1)
        self.assertEqual(ClassicPositionProperty.get_letter_multiplier(ClassicPositionProperty.L2), 2)
        self.assertEqual(ClassicPositionProperty.get_letter_multiplier(ClassicPositionProperty.L3), 3)

    def test_class_word_multiplier(self):
        self.assertEqual(ClassicPositionProperty.get_word_multiplier(ClassicPositionProperty.normal), 1)
        self.assertEqual(ClassicPositionProperty.get_word_multiplier(ClassicPositionProperty.DL), 1)
        self.assertEqual(ClassicPositionProperty.get_word_multiplier(ClassicPositionProperty.W2), 2)
        self.assertEqual(ClassicPositionProperty.get_word_multiplier(ClassicPositionProperty.W3), 3)
        self.assertEqual(ClassicPositionProperty.get_word_multiplier(ClassicPositionProperty.W4), 4)

    def test_object_letter_multiplier(self):
        self.assertEqual(ClassicPositionProperty.normal.letter_multiplier(), 1)
        self.assertEqual(ClassicPositionProperty.DW.letter_multiplier(), 1)
        self.assertEqual(ClassicPositionProperty.L2.letter_multiplier(), 2)
        self.assertEqual(ClassicPositionProperty.L3.letter_multiplier(), 3)

    def test_object_word_multiplier(self):
        self.assertEqual(ClassicPositionProperty.normal.word_multiplier(), 1)
        self.assertEqual(ClassicPositionProperty.DL.word_multiplier(), 1)
        self.assertEqual(ClassicPositionProperty.W2.word_multiplier(), 2)
        self.assertEqual(ClassicPositionProperty.W3.word_multiplier(), 3)
        self.assertEqual(ClassicPositionProperty.W4.word_multiplier(), 4)


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
        pos = Position(2, 10, ClassicPositionProperty.normal)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 10)

    def test_property_default(self):
        self.assertEqual(Position(1, 1, ClassicPositionProperty.normal).property,
                         ClassicPositionProperty.normal)

    def test_property_construction_and_setter(self):
        pos = Position(1, 1, ClassicPositionProperty.CENTER)
        self.assertEqual(pos.property, ClassicPositionProperty.CENTER)
        pos.property = ClassicPositionProperty.DL
        self.assertEqual(pos.property, ClassicPositionProperty.DL)


if __name__ == "__main__":
    unittest.main()
