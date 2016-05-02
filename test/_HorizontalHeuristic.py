import unittest

from game.ConnectFour import ConnectFour
from game.Heuristic import heuristic


class _HorizontalHeuristic(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.state = ConnectFour().initial
        cls.problemPlayer = 'X'

    def test_when_whe_got_empty_board_heuristic_should_be_0(self):
        self.assertEqual(heuristic(self.state, self.problemPlayer), 0)

    def test_when_whe_got_a_single_token_in_the_board_heuristic_should_be_1(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.moves.remove((4, 1))
        self.assertEqual(heuristic(self.state, self.problemPlayer), 1)

    def test_when_whe_got_a_single_enemy_token_in_the_board_heuristic_should_be_minus_1(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.moves.remove((4, 1))
        self.assertEqual(heuristic(self.state, self.problemPlayer), -1)