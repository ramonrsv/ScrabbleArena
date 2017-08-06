import unittest
from lib.position import PositionAttribute, Position
from lib.position import ClassicPositionAttribute


class TestPositionAttributeUsingClassicPosition(unittest.TestCase):
    def test_simple_isinstance(self):
        self.assertIsInstance(ClassicPositionAttribute.normal, ClassicPositionAttribute)
        self.assertIsInstance(ClassicPositionAttribute.CENTER, ClassicPositionAttribute)
        self.assertIsInstance(ClassicPositionAttribute.DW, ClassicPositionAttribute)
        self.assertIsInstance(ClassicPositionAttribute.W3, ClassicPositionAttribute)

    def test_equal_enums(self):
        self.assertEqual(ClassicPositionAttribute.L2, ClassicPositionAttribute.DL)
        self.assertEqual(ClassicPositionAttribute.L3, ClassicPositionAttribute.TL)
        self.assertEqual(ClassicPositionAttribute.W2, ClassicPositionAttribute.DW)
        self.assertEqual(ClassicPositionAttribute.W3, ClassicPositionAttribute.TW)

    def test_bool_op(self):
        self.assertFalse(True if ClassicPositionAttribute.normal.value else False)
        self.assertTrue(True if ClassicPositionAttribute.CENTER.value else False)
        self.assertFalse(bool(ClassicPositionAttribute.normal.value))
        self.assertTrue(bool(ClassicPositionAttribute.CENTER.value))

    def test_class_letter_multiplier(self):
        self.assertEqual(ClassicPositionAttribute.get_letter_multiplier(ClassicPositionAttribute.normal), 1)
        self.assertEqual(ClassicPositionAttribute.get_letter_multiplier(ClassicPositionAttribute.DW), 1)
        self.assertEqual(ClassicPositionAttribute.get_letter_multiplier(ClassicPositionAttribute.L2), 2)
        self.assertEqual(ClassicPositionAttribute.get_letter_multiplier(ClassicPositionAttribute.L3), 3)

    def test_class_word_multiplier(self):
        self.assertEqual(ClassicPositionAttribute.get_word_multiplier(ClassicPositionAttribute.normal), 1)
        self.assertEqual(ClassicPositionAttribute.get_word_multiplier(ClassicPositionAttribute.DL), 1)
        self.assertEqual(ClassicPositionAttribute.get_word_multiplier(ClassicPositionAttribute.W2), 2)
        self.assertEqual(ClassicPositionAttribute.get_word_multiplier(ClassicPositionAttribute.W3), 3)
        self.assertEqual(ClassicPositionAttribute.get_word_multiplier(ClassicPositionAttribute.W4), 4)

    def test_object_letter_multiplier(self):
        self.assertEqual(ClassicPositionAttribute.normal.letter_multiplier(), 1)
        self.assertEqual(ClassicPositionAttribute.DW.letter_multiplier(), 1)
        self.assertEqual(ClassicPositionAttribute.L2.letter_multiplier(), 2)
        self.assertEqual(ClassicPositionAttribute.L3.letter_multiplier(), 3)

    def test_object_word_multiplier(self):
        self.assertEqual(ClassicPositionAttribute.normal.word_multiplier(), 1)
        self.assertEqual(ClassicPositionAttribute.DL.word_multiplier(), 1)
        self.assertEqual(ClassicPositionAttribute.W2.word_multiplier(), 2)
        self.assertEqual(ClassicPositionAttribute.W3.word_multiplier(), 3)
        self.assertEqual(ClassicPositionAttribute.W4.word_multiplier(), 4)


class TestNewPositionAttribute(unittest.TestCase):
        class NewPositionAttribute(PositionAttribute):
            T1 = 0
            T2 = 1

            @classmethod
            def _letter_multiplier_dict(cls):
                return cls._get_full_letter_multiplier_dict({cls.T1: 1, cls.T2: 2}, default_value=1)

            @classmethod
            def _word_multiplier_dict(cls):
                return cls._get_full_word_multiplier_dict({cls.T1: 10}, default_value=1)

        def test_inherited_class_isinstance(self):
            self.assertIsInstance(self.NewPositionAttribute.T1, self.NewPositionAttribute)
            self.assertIsInstance(self.NewPositionAttribute.T2, self.NewPositionAttribute)

        def test_base_class_isinstance(self):
            self.assertIsInstance(self.NewPositionAttribute.T1, PositionAttribute)
            self.assertIsInstance(self.NewPositionAttribute.T2, PositionAttribute)

        def test_different_enum_attribute_multiplier(self):
            self.assertEqual(self.NewPositionAttribute.get_word_multiplier(self.NewPositionAttribute.T1), 10)
            self.assertEqual(self.NewPositionAttribute.T1.letter_multiplier(), 1)


class TestPosition(unittest.TestCase):
    def test_simple_construction(self):
        pos = Position(2, 10, ClassicPositionAttribute.normal)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 10)

    def test_attribute_default(self):
        self.assertEqual(Position(1, 1, ClassicPositionAttribute.normal).attribute,
                         ClassicPositionAttribute.normal)

    def test_attribute_construction_and_setter(self):
        pos = Position(1, 1, ClassicPositionAttribute.CENTER)
        self.assertEqual(pos.attribute, ClassicPositionAttribute.CENTER)
        pos.attribute = ClassicPositionAttribute.DL
        self.assertEqual(pos.attribute, ClassicPositionAttribute.DL)


if __name__ == "__main__":
    unittest.main()
