import unittest
from board_position import  PosProperty, Position
from board import BoardConfiguration


class TestBoardConfiguration(unittest.TestCase):
    def setUp(self):
        self.special_positions_1 = [Position(1, 1, PosProperty.DL),
                                    Position(2, 2, PosProperty.TL)]
        self.special_positions_2 = [Position(4, 4, PosProperty.TW),
                                    Position(5, 5, PosProperty.W4)]
        self.special_positions_3 = [Position(1, 1), Position(3, 1), Position(1, 3), Position(3, 3)]
        self.special_positions_3_corner_symmetry = [Position(1, 1), Position(3, 1), Position(1, 3), Position(3, 3),
                                                    Position(5, 1), Position(5, 3),
                                                    Position(1, 5), Position(3, 5), Position(5, 5)]

    def test_simple_construction(self):
        bc = BoardConfiguration(15, 15)
        self.assertEqual((bc.width, bc.height), (15, 15))
        bc = BoardConfiguration(1, 15)
        self.assertEqual((bc.width, bc.height), (1, 15))

    def test_dimension_setters(self):
        bc = BoardConfiguration(15, 15)
        self.assertEqual((bc.width, bc.height), (15, 15))
        bc.width = 1
        bc.height = 2
        self.assertEqual((bc.width, bc.height), (1, 2))

    def test_bad_dimension_construction(self):
        self.assertRaises(TypeError, lambda: BoardConfiguration(-1, 0))
        self.assertRaises(TypeError, lambda: BoardConfiguration('a', 'b'))

    def test_bad_dimension_reassignment(self):
        bc = BoardConfiguration(15, 15)
        with self.assertRaises(TypeError):
            bc.width = -1

    def test_special_positions_construction(self):
        bc = BoardConfiguration(15, 15, self.special_positions_1)
        self.assertListEqual(bc.special_positions, self.special_positions_1)

    def test_special_positions_reassignment(self):
        bc = BoardConfiguration(15, 15, self.special_positions_1)
        bc.special_positions = self.special_positions_2
        self.assertListEqual(bc.special_positions, self.special_positions_2)

    def test_center_coo(self):
        self.assertEqual(BoardConfiguration.center_coo(15, 15), (8, 8))
        self.assertEqual(BoardConfiguration.center_coo(10, 10), (None, None))
        self.assertEqual(BoardConfiguration.center_coo(15, 10), (8, None))

    def test_in_bounds(self):
        self.assertTrue(BoardConfiguration.in_bounds(Position(1, 2), {'x': (1, 4), 'y': (1, 4)}))
        self.assertFalse(BoardConfiguration.in_bounds(Position(4, 6), {'x': (1, 4), 'y': (1, 4)}))
        self.assertTrue(BoardConfiguration.in_bounds(Position(4, 4), {'x': (1, 4), 'y': (1, 4)}))

    def test_quadrant_bound(self):
        self.assertEqual(BoardConfiguration._quadrant_bounds(4, 4), {
            1: {'x': (3, 4), 'y': (1, 2)},
            2: {'x': (1, 2), 'y': (1, 2)},
            3: {'x': (1, 2), 'y': (3, 4)},
            4: {'x': (3, 4), 'y': (3, 4)}})

        self.assertEqual(BoardConfiguration._quadrant_bounds(5, 5), {
            1: {'x': (4, 5), 'y': (1, 2)},
            2: {'x': (1, 2), 'y': (1, 2)},
            3: {'x': (1, 2), 'y': (4, 5)},
            4: {'x': (4, 5), 'y': (4, 5)}})

        self.assertEqual(BoardConfiguration._quadrant_bounds(5, 5, inclusive=True), {
            1: {'x': (3, 5), 'y': (1, 3)},
            2: {'x': (1, 3), 'y': (1, 3)},
            3: {'x': (1, 3), 'y': (3, 5)},
            4: {'x': (3, 5), 'y': (3, 5)}})

    def test_find_quadrant(self):
        self.assertEqual(BoardConfiguration._find_quadrant(Position(5, 1), 5, 5), 1)
        self.assertEqual(BoardConfiguration._find_quadrant(Position(1, 1), 5, 5), 2)
        self.assertEqual(BoardConfiguration._find_quadrant(Position(1, 5), 5, 5), 3)
        self.assertEqual(BoardConfiguration._find_quadrant(Position(5, 5), 5, 5), 4)
        self.assertEqual(BoardConfiguration._find_quadrant(Position(3, 1), 5, 5), None)
        self.assertEqual(BoardConfiguration._find_quadrant(Position(1, 3), 5, 5), None)
        self.assertEqual(BoardConfiguration._find_quadrant(Position(3, 3), 5, 5), None)

    def test_mirror_position(self):
        self.assertEqual(BoardConfiguration._mirror_position(Position(1, 1), 'x', 5, 5), Position(5, 1))
        self.assertEqual(BoardConfiguration._mirror_position(Position(1, 1), 'y', 5, 5), Position(1, 5))
        self.assertEqual(BoardConfiguration._mirror_position(Position(3, 3), 'x', 5, 5), None)
        self.assertEqual(BoardConfiguration._mirror_position(Position(3, 3), 'y', 5, 5), None)
        self.assertEqual(BoardConfiguration._mirror_position(Position(3, 1), 'x', 5, 5), None)
        self.assertEqual(BoardConfiguration._mirror_position(Position(3, 1), 'y', 5, 5), Position(3, 5))

    def test_from_corners_symmetry(self):
        bc = BoardConfiguration.from_corners_symmetry(5, 5, self.special_positions_3)
        self.assertListEqual(sorted(bc.special_positions), sorted(self.special_positions_3_corner_symmetry))

if __name__ == "__main__":
    unittest.main()
