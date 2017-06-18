import unittest
from lib.dimension_and_coordinate import Coordinate, Dimension


class TestCoordinate(unittest.TestCase):
    def test_simple_construction(self):
        pos = Coordinate(2, 10)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 10)

    def test_x_to_alpha(self):
        self.assertEqual(Coordinate.x_to_alpha(1), 'A')
        self.assertEqual(Coordinate.x_to_alpha(26), 'Z')

    def test_alpha_to_x(self):
        self.assertEqual(Coordinate.alpha_to_x('A'), 1)
        self.assertEqual(Coordinate.alpha_to_x('a'), 1)
        self.assertEqual(Coordinate.alpha_to_x('Z'), 26)
        self.assertEqual(Coordinate.alpha_to_x('z'), 26)

    def test_x_to_alpha_type_error(self):
        self.assertRaises(TypeError, lambda: Coordinate.x_to_alpha('A'))

    def test_x_to_alpha_value_error(self):
        self.assertRaises(ValueError, lambda: Coordinate.x_to_alpha(27))

    def test_alpha_to_x_type_error(self):
        self.assertRaises(TypeError, lambda: Coordinate.alpha_to_x('\n'))
        self.assertRaises(TypeError, lambda: Coordinate.alpha_to_x(1))

    def test_alpha_construction(self):
        pos = Coordinate('A', 3)
        self.assertEqual(pos.x, 1)
        self.assertEqual(pos.y, 3)

    def test_alpha_property(self):
        pos = Coordinate('B', 10)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.x_alpha, 'B')
        self.assertEqual(pos.y, 10)

    def test_alpha_setter(self):
        pos = Coordinate(1, 1)
        self.assertEqual(pos.x, 1)
        self.assertEqual(pos.y, 1)
        pos.x = 'B'
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.x_alpha, 'B')
        pos.x_alpha = 'C'
        self.assertEqual(pos.x, 3)
        self.assertEqual(pos.x_alpha, 'C')

    def test_coo(self):
        self.assertEqual(Coordinate(1, 1).coo, (1, 1))
        self.assertEqual(Coordinate('Z', 10).coo, (26, 10))


class TestDimension(unittest.TestCase):
    def test_simple_construction(self):
        bc = Dimension(15, 15)
        self.assertEqual((bc.width, bc.height), (15, 15))
        bc = Dimension(1, 15)
        self.assertEqual((bc.width, bc.height), (1, 15))

    def test_dimension_setters(self):
        bc = Dimension(15, 15)
        self.assertEqual((bc.width, bc.height), (15, 15))
        bc.width = 1
        bc.height = 2
        self.assertEqual((bc.width, bc.height), (1, 2))

    def test_bad_dimension_construction(self):
        self.assertRaises(TypeError, lambda: Dimension(-1, 0))
        self.assertRaises(TypeError, lambda: Dimension('a', 'b'))

    def test_bad_dimension_reassignment(self):
        bc = Dimension(15, 15)
        with self.assertRaises(TypeError):
            bc.width = -1

    def test_center_coo(self):
        self.assertEqual(Dimension.center_coo(15, 15), (8, 8))
        self.assertEqual(Dimension.center_coo(10, 10), (None, None))
        self.assertEqual(Dimension.center_coo(15, 10), (8, None))

    def test_in_bounds(self):
        self.assertTrue(Dimension.in_bounds((1, 2), {'x': (1, 4), 'y': (1, 4)}))
        self.assertFalse(Dimension.in_bounds((4, 6), {'x': (1, 4), 'y': (1, 4)}))
        self.assertTrue(Dimension.in_bounds((4, 4), {'x': (1, 4), 'y': (1, 4)}))

if __name__ == "__main__":
    unittest.main()
