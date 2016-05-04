from game.heuristics.HorizontalHeuristic import HorizontalHeuristic
from game.heuristics.VerticalHeuristic import VerticalHeuristic


def heuristic(state, problem_player):
    heuristic_value = 0
    other_player = "O" if problem_player == "X" else "X"
    heuristic_value += VerticalHeuristic(state, problem_player, other_player).heuristic()
    if heuristic_value == -float('inf') or heuristic_value == float('inf'):
        return heuristic_value
    heuristic_value += HorizontalHeuristic(state, problem_player, other_player).heuristic()
    if heuristic_value == -float('inf') or heuristic_value == float('inf'):
        return heuristic_value
    return heuristic_value
