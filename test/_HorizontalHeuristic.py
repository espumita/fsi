import unittest

from game.ConnectFour import ConnectFour
from game.heuristics.HorizontalHeuristic import HorizontalHeuristic


class _HorizontalHeuristic(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.state = ConnectFour().initial
        cls.problemPlayer = 'X'
        cls.otherPlayer = "O"

    def horizontalBoardHeuristic(self):
        heuristicValue = 0
        for key in self.state.board:
            heuristicValue += HorizontalHeuristic(self.state, self.problemPlayer, self.otherPlayer).heuristicIn(key)
            if heuristicValue == -float('inf') or heuristicValue == float('inf'):
                return heuristicValue
        return heuristicValue

    def test_when_whe_got_empty_board_heuristic_should_be_0(self):
        self.assertEqual(self.horizontalBoardHeuristic(), 0)

    def test_when_whe_got_a_single_token_in_the_board_heuristic_should_be_1(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.moves.remove((4, 1))
        self.assertEqual(self.horizontalBoardHeuristic(), 1)

    def test_when_whe_got_a_single_enemy_token_in_the_board_heuristic_should_be_minus_1(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.moves.remove((4, 1))
        self.assertEqual(self.horizontalBoardHeuristic(), -1)