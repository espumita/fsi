import unittest

from game.ConnectFour import ConnectFour
from game.Heuristics import firstHeuristics


class _Heuristics(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.state = ConnectFour().initial

    def test_when_whe_got_empty_board_heuristics_should_be_0(self):
        self.assertEqual(firstHeuristics(self.state, 'X'), 0)

    def test_when_whe_got_a_single_token_in_the_board_heuristics_should_be_1(self):
        self.state.board.setdefault((1, 1), 'X')
        self.state.moves.remove((1, 1))
        self.assertEqual(firstHeuristics(self.state, 'X'), 1)

    def test_when_whe_got_a_single_enemy_token_in_the_board_heuristics_should_be_minus_1(self):
        self.state.board.setdefault((1, 1), 'O')
        self.state.moves.remove((1, 1))
        self.assertEqual(firstHeuristics(self.state, 'X'), -1)