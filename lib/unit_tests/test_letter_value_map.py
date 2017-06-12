import unittest
from lib.letter_value_map import LetterValueMap


class TestLetterValueMap(unittest.TestCase):
    def setUp(self):
        self.sample_lvm1 = LetterValueMap({
            " ": 0,
            'A': 1,
            'B': 3,
            'C': 3,
            'D': 2,
            'E': 1
        })

    def test_BLANK_property(self):
        self.assertIsInstance(LetterValueMap.BLANK, str)
        self.assertIsInstance(self.sample_lvm1.BLANK, str)
        self.assertEqual(len(LetterValueMap.BLANK), 1)
        self.assertEqual(len(self.sample_lvm1.BLANK), 1)

    def test_all_letters_contained(self):
        self.assertEqual({" ", 'A', 'B', 'C', 'D', 'E'}, set(self.sample_lvm1.all_letters()))

    def test_get_letter_value_with_present_letter(self):
        self.assertEqual(self.sample_lvm1.get_letter_value('A'), 1)
        self.assertEqual(self.sample_lvm1.get_letter_value(self.sample_lvm1.BLANK), 0)
        self.assertEqual(self.sample_lvm1.get_letter_value(LetterValueMap.BLANK), 0)

    def test_get_letter_value_with_missing_letter(self):
        self.assertRaises(KeyError, lambda: self.sample_lvm1.get_letter_value('Z'))

    def test_is_letter_valid_with_valid_letter(self):
        self.assertTrue(self.sample_lvm1.is_letter_valid('A'))
        self.assertTrue(self.sample_lvm1.is_letter_valid('E'))
        self.assertTrue(self.sample_lvm1.is_letter_valid(self.sample_lvm1.BLANK))
        self.assertTrue(self.sample_lvm1.is_letter_valid(LetterValueMap.BLANK))

    def test_is_letter_valid_with_invalid_letter(self):
        self.assertFalse(self.sample_lvm1.is_letter_valid('Z'))

    def test_failed_construction_invalid_letter(self):
        self.assertRaises(TypeError, lambda: LetterValueMap({4: 3}))

    def test_failed_construction_invalid_value(self):
        self.assertRaises(TypeError, lambda: LetterValueMap({'A': 'A'}))

    def test_failed_construction_blank_not_present(self):
        self.assertRaises(ValueError, lambda: LetterValueMap({'A': 3}))

if __name__ == "__main__":
    unittest.main()
