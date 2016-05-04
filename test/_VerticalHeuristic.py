from game.ConnectFour import ConnectFour
from game.heuristics.VerticalHeuristic import VerticalHeuristic
import unittest


class _VerticalHeuristic(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.state = ConnectFour().initial
        cls.problemPlayer = 'X'
        cls.otherPlayer = 'O'

    def test_when_whe_got_empty_board_heuristic_should_be_0(self):
        self.assertEqual(self.vertical_board_heuristic(), 0)

    def test_when_whe_got_a_single_token_in_the_board_heuristic_should_be_10(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.moves.remove((4, 1))
        self.assertEqual(self.vertical_board_heuristic(), 10)

    def test_when_whe_got_a_single_enemy_token_in_the_board_heuristic_should_be_minus_10(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.moves.remove((4, 1))
        self.assertEqual(self.vertical_board_heuristic(), -10)

    def test_when_whe_got_a_vertical_connection_of_two_tokens_heuristic_should_be_250(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((4, 2), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((4, 2))
        self.assertEqual(self.vertical_board_heuristic(), 250)

    def test_when_whe_got_a_vertical_connection_of_two_enemy_tokens_heuristic_should_be_minus_250(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((4, 2), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((4, 2))
        self.assertEqual(self.vertical_board_heuristic(), -250)

    def test_when_whe_got_a_vertical_connection_of_three_tokens_heuristic_should_be_490(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((4, 2), 'X')
        self.state.board.setdefault((4, 3), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((4, 2))
        self.state.moves.remove((4, 3))
        self.assertEqual(self.vertical_board_heuristic(), 490)

    def test_when_whe_got_a_vertical_connection_of_three_enemy_tokens_heuristic_should_be_minus_490(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((4, 2), 'O')
        self.state.board.setdefault((4, 3), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((4, 2))
        self.state.moves.remove((4, 3))
        self.assertEqual(self.vertical_board_heuristic(), -490)

    def test_when_whe_got_a_vertical_connection_of_four_tokens_heuristic_should_be_infinity(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((4, 2), 'X')
        self.state.board.setdefault((4, 3), 'X')
        self.state.board.setdefault((4, 4), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((4, 2))
        self.state.moves.remove((4, 3))
        self.state.moves.remove((4, 4))
        self.assertEqual(self.vertical_board_heuristic(), float('inf'))

    def test_when_whe_got_a_vertical_connection_of_four_enemy_tokens_heuristic_should_be_minus_infinity(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((4, 2), 'O')
        self.state.board.setdefault((4, 3), 'O')
        self.state.board.setdefault((4, 4), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((4, 2))
        self.state.moves.remove((4, 3))
        self.state.moves.remove((4, 4))
        self.assertEqual(self.vertical_board_heuristic(), -float('inf'))

    def test_when_you_block_a_single_vertical_connection_heuristic_should_be_10(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((4, 2), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((4, 2))
        self.assertEqual(self.vertical_board_heuristic(), 10)

    def test_when_you_get_blocked_in_a_single_vertical_connection_heuristic_should_be_minus_10(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((4, 2), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((4, 2))
        self.assertEqual(self.vertical_board_heuristic(), -10)

    def test_when_you_block_a_two_vertical_connection_heuristic_should_be_10(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((4, 2), 'O')
        self.state.board.setdefault((4, 3), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((4, 2))
        self.state.moves.remove((4, 3))
        self.assertEqual(self.vertical_board_heuristic(), 10)

    def test_when_you_get_blocked_in_a_two_vertical_connection_heuristic_should_be_minus_10(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((4, 2), 'X')
        self.state.board.setdefault((4, 3), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((4, 2))
        self.state.moves.remove((4, 3))
        self.assertEqual(self.vertical_board_heuristic(), -10)

    def test_when_you_block_a_three_vertical_connection_heuristic_should_be_10(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((4, 2), 'O')
        self.state.board.setdefault((4, 3), 'O')
        self.state.board.setdefault((4, 4), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((4, 2))
        self.state.moves.remove((4, 3))
        self.state.moves.remove((4, 4))
        self.assertEqual(self.vertical_board_heuristic(), 10)

    def test_when_you_get_blocked_in_a_three_vertical_connection_heuristic_should_be_minus_10(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((4, 2), 'X')
        self.state.board.setdefault((4, 3), 'X')
        self.state.board.setdefault((4, 4), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((4, 2))
        self.state.moves.remove((4, 3))
        self.state.moves.remove((4, 4))
        self.assertEqual(self.vertical_board_heuristic(), -10)

    def vertical_board_heuristic(self):
        return VerticalHeuristic(self.state, self.problemPlayer, self.otherPlayer).heuristic()
