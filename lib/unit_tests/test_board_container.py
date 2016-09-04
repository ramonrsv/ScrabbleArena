import unittest
from ..settings import Words_with_friends_board_configuration
from ..position import Position, PosProperty
from ..board_container import BoardContainer


class TestBoardContainer(unittest.TestCase):
    def test_simple_construction(self):
        bc = BoardContainer(Words_with_friends_board_configuration)
        self.assertEqual((bc.height, bc.width), (15, 15))

    def test_positions_length(self):
        bc = BoardContainer(Words_with_friends_board_configuration)
        self.assertEqual(sum(1 for _ in bc.positions()), 15 * 15)

    def test_get_position(self):
        bc = BoardContainer(Words_with_friends_board_configuration)
        center = bc.get_position((8, 8))
        self.assertIsInstance(center, Position)
        self.assertEqual(center.coo, (8, 8))
        self.assertEqual(center.property, PosProperty.CENTER)

    def test_get_position_alpha(self):
        bc = BoardContainer(Words_with_friends_board_configuration)
        d2 = bc.get_position(('D', 1))
        self.assertIsInstance(d2, Position)
        self.assertEqual(d2.coo, (4, 1))
        self.assertEqual(d2.coo_alpha, ('D', 1))
        self.assertEqual(d2.property, PosProperty.W3)


if __name__ == "__main__":
    unittest.main()
