import unittest
from ..dimension_coordinate_properties import CoordinateProperty, DimensionProperty


class TestCoordinateProperty(unittest.TestCase):
    def test_simple_construction(self):
        pos = CoordinateProperty(2, 10)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 10)

    def test_x_to_alpha(self):
        self.assertEqual(CoordinateProperty.x_to_alpha(1), 'A')
        self.assertEqual(CoordinateProperty.x_to_alpha(26), 'Z')

    def test_alpha_to_x(self):
        self.assertEqual(CoordinateProperty.alpha_to_x('A'), 1)
        self.assertEqual(CoordinateProperty.alpha_to_x('a'), 1)
        self.assertEqual(CoordinateProperty.alpha_to_x('Z'), 26)
        self.assertEqual(CoordinateProperty.alpha_to_x('z'), 26)

    def test_x_to_alpha_type_error(self):
        self.assertRaises(TypeError, lambda: CoordinateProperty.x_to_alpha('A'))

    def test_x_to_alpha_value_error(self):
        self.assertRaises(ValueError, lambda: CoordinateProperty.x_to_alpha(27))

    def test_alpha_to_x_type_error(self):
        self.assertRaises(TypeError, lambda: CoordinateProperty.alpha_to_x('\n'))
        self.assertRaises(TypeError, lambda: CoordinateProperty.alpha_to_x(1))

    def test_alpha_construction(self):
        pos = CoordinateProperty('A', 3)
        self.assertEqual(pos.x, 1)
        self.assertEqual(pos.y, 3)

    def test_alpha_property(self):
        pos = CoordinateProperty('B', 10)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.x_alpha, 'B')
        self.assertEqual(pos.y, 10)

    def test_alpha_setter(self):
        pos = CoordinateProperty(1, 1)
        self.assertEqual(pos.x, 1)
        self.assertEqual(pos.y, 1)
        pos.x = 'B'
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.x_alpha, 'B')
        pos.x_alpha = 'C'
        self.assertEqual(pos.x, 3)
        self.assertEqual(pos.x_alpha, 'C')

    def test_coo(self):
        self.assertEqual(CoordinateProperty(1, 1).coo, (1, 1))
        self.assertEqual(CoordinateProperty('Z', 10).coo, (26, 10))


class TestDimensionProperty(unittest.TestCase):
    def test_simple_construction(self):
        bc = DimensionProperty(15, 15)
        self.assertEqual((bc.width, bc.height), (15, 15))
        bc = DimensionProperty(1, 15)
        self.assertEqual((bc.width, bc.height), (1, 15))

    def test_dimension_setters(self):
        bc = DimensionProperty(15, 15)
        self.assertEqual((bc.width, bc.height), (15, 15))
        bc.width = 1
        bc.height = 2
        self.assertEqual((bc.width, bc.height), (1, 2))

    def test_bad_dimension_construction(self):
        self.assertRaises(TypeError, lambda: DimensionProperty(-1, 0))
        self.assertRaises(TypeError, lambda: DimensionProperty('a', 'b'))

    def test_bad_dimension_reassignment(self):
        bc = DimensionProperty(15, 15)
        with self.assertRaises(TypeError):
            bc.width = -1


if __name__ == "__main__":
    unittest.main()
