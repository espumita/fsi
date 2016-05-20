from game.ConnectFour import ConnectFour
from game.heuristics.HorizontalHeuristic import HorizontalHeuristic
import unittest


class _HorizontalHeuristic(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.state = ConnectFour().initial
        cls.problemPlayer = 'X'
        cls.otherPlayer = "O"

    def test_when_whe_got_empty_board_heuristic_should_be_0(self):
        self.assertEqual(self.horizontal_heuristic(), 0)

    def test_when_whe_got_a_horizontal_connection_of_four_tokens_heuristic_should_be_infinity(self):
        self.add_tokens({
            (1, 1): 'X',
            (2, 1): 'X',
            (3, 1): 'X',
            (4, 1): 'X'
        })
        self.assertEqual(self.horizontal_heuristic(), float('inf'))

    def test_when_whe_got_an_enemy_horizontal_connection_of_four_tokens_heuristic_should_be_minus_infinity(self):
        self.add_tokens({
            (1, 1): 'O',
            (2, 1): 'O',
            (3, 1): 'O',
            (4, 1): 'O'
        })
        self.assertEqual(self.horizontal_heuristic(), -float('inf'))

    def horizontal_heuristic(self):
        return HorizontalHeuristic(self.state, self.problemPlayer, self.otherPlayer).heuristic()

    def add_tokens(self, tokens):
        for key in tokens:
            self.state.board.setdefault(key, tokens[key])
            self.state.moves.remove(key)
