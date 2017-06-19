import unittest
from lib.game_types.board_configurations import Words_with_friends_board_configuration
from lib.position import Position, ClassicPositionProperty
from lib.board import Board, BoardConfiguration


class TestBoard(unittest.TestCase):
    def test_simple_construction(self):
        bc = Board(Words_with_friends_board_configuration)
        self.assertEqual((bc.height, bc.width), (15, 15))

    def test_positions_length(self):
        bc = Board(Words_with_friends_board_configuration)
        self.assertEqual(sum(1 for _ in bc.positions()), 15 * 15)

    def test_get_position(self):
        bc = Board(Words_with_friends_board_configuration)
        center = bc.get_position((8, 8))
        self.assertIsInstance(center, Position)
        self.assertEqual(center.coo, (8, 8))
        self.assertEqual(center.property, ClassicPositionProperty.CENTER)

    def test_get_position_alpha(self):
        bc = Board(Words_with_friends_board_configuration)
        d2 = bc.get_position(('D', 1))
        self.assertIsInstance(d2, Position)
        self.assertEqual(d2.coo, (4, 1))
        self.assertEqual(d2.coo_alpha, ('D', 1))
        self.assertEqual(d2.property, ClassicPositionProperty.W3)


class TestBoardConfiguration(unittest.TestCase):
    def setUp(self):
        self.special_positions_1 = [Position(1, 1, ClassicPositionProperty.DL),
                                    Position(2, 2, ClassicPositionProperty.TL)]
        self.special_positions_2 = [Position(4, 4, ClassicPositionProperty.TW),
                                    Position(5, 5, ClassicPositionProperty.W4)]
        self.special_positions_3 = [Position(1, 1), Position(3, 1), Position(1, 3), Position(3, 3)]
        self.special_positions_3_corner_symmetry = [Position(1, 1), Position(3, 1), Position(1, 3), Position(3, 3),
                                                    Position(5, 1), Position(5, 3),
                                                    Position(1, 5), Position(3, 5), Position(5, 5)]
        self.bad_special_positions = [Position(1, 1), Position(5, 5)]  # Will cause duplicates in from_corners_symmetry

    def test_simple_construction(self):
        bc = BoardConfiguration(15, 15)
        self.assertEqual((bc.width, bc.height), (15, 15))
        bc = BoardConfiguration(1, 15)
        self.assertEqual((bc.width, bc.height), (1, 15))

    def test_special_positions_construction(self):
        bc = BoardConfiguration(15, 15, self.special_positions_1)
        self.assertListEqual(bc.special_positions, self.special_positions_1)

    def test_special_positions_reassignment(self):
        bc = BoardConfiguration(15, 15, self.special_positions_1)
        bc.special_positions = self.special_positions_2
        self.assertListEqual(bc.special_positions, self.special_positions_2)

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

    def test_bad_from_corners_symmetry(self):
        with self.assertRaises(ValueError):
            BoardConfiguration.from_corners_symmetry(5, 5, self.bad_special_positions)


if __name__ == "__main__":
    unittest.main()
