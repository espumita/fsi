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
        self.assertEqual(self.horizontal_board_heuristic(), 0)

    def test_when_whe_got_a_single_token_in_the_board_heuristic_should_be_20(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.moves.remove((4, 1))
        self.assertEqual(self.horizontal_board_heuristic(), 20)

    def test_when_whe_got_a_single_enemy_token_in_the_board_heuristic_should_be_minus_20(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.moves.remove((4, 1))
        self.assertEqual(self.horizontal_board_heuristic(), -20)

    def test_when_whe_got_a_horizontal_connection_of_two_tokens_heuristic_should_be_260(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((5, 1), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.assertEqual(self.horizontal_board_heuristic(), 260)

    def test_when_whe_got_a_horizontal_connection_of_two_enemy_tokens_heuristic_should_be_minus_260(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((5, 1), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.assertEqual(self.horizontal_board_heuristic(), -260)

    def test_when_whe_got_only_two_different_tokens_heuristic_should_be_0(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((5, 1), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.assertEqual(self.horizontal_board_heuristic(), 0)

    def test_when_whe_got_only_two_different_tokens_again_heuristic_should_be_0(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((5, 1), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.assertEqual(self.horizontal_board_heuristic(), 0)

    def test_when_whe_got_a_horizontal_connection_of_three_tokens_heuristic_should_be_500(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((5, 1), 'X')
        self.state.board.setdefault((6, 1), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.state.moves.remove((6, 1))
        self.assertEqual(self.horizontal_board_heuristic(), 500)

    def test_when_whe_got_a_horizontal_connection_of_three_enemy_tokens_heuristic_should_be_minus_500(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((5, 1), 'O')
        self.state.board.setdefault((6, 1), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.state.moves.remove((6, 1))
        self.assertEqual(self.horizontal_board_heuristic(), -500)

    def test_when_you_get_blocked_from_the_right_in_a_two_horizontal_connection_heuristic_should_be_6(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((5, 1), 'X')
        self.state.board.setdefault((6, 1), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.state.moves.remove((6, 1))
        self.assertEqual(self.horizontal_board_heuristic(), 6)

    def test_when_you_get_blocked_from_the_left_in_a_two_horizontal_connection_heuristic_should_be_230(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((5, 1), 'X')
        self.state.board.setdefault((6, 1), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.state.moves.remove((6, 1))
        self.assertEqual(self.horizontal_board_heuristic(), 230)

    def test_when_you_block_from_the_right_in_a_two_horizontal_connection_heuristic_should_be_minus_6(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((5, 1), 'O')
        self.state.board.setdefault((6, 1), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.state.moves.remove((6, 1))
        self.assertEqual(self.horizontal_board_heuristic(), -6)

    def test_when_you_block_from_the_left_in_a_two_horizontal_connection_heuristic_should_be_minus_6(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((5, 1), 'O')
        self.state.board.setdefault((6, 1), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.state.moves.remove((6, 1))
        self.assertEqual(self.horizontal_board_heuristic(), -6)

    def test_when_whe_got_a_horizontal_connection_of_four_tokens_heuristic_should_be_infinity(self):
        self.state.board.setdefault((4, 1), 'X')
        self.state.board.setdefault((5, 1), 'X')
        self.state.board.setdefault((6, 1), 'X')
        self.state.board.setdefault((7, 1), 'X')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.state.moves.remove((6, 1))
        self.state.moves.remove((7, 1))
        self.assertEqual(self.horizontal_board_heuristic(), float('inf'))

    def test_when_whe_got_a_horizontal_connection_of_four_enemy_tokens_heuristic_should_be_minus_infinity(self):
        self.state.board.setdefault((4, 1), 'O')
        self.state.board.setdefault((5, 1), 'O')
        self.state.board.setdefault((6, 1), 'O')
        self.state.board.setdefault((7, 1), 'O')
        self.state.moves.remove((4, 1))
        self.state.moves.remove((5, 1))
        self.state.moves.remove((6, 1))
        self.state.moves.remove((7, 1))
        self.assertEqual(self.horizontal_board_heuristic(), -float('inf'))

    def horizontal_board_heuristic(self):
        return HorizontalHeuristic(self.state, self.problemPlayer, self.otherPlayer).heuristic()
