from game.heuristics.HorizontalHeuristic import HorizontalHeuristic
from game.heuristics.VerticalHeuristic import VerticalHeuristic


def player(state, key, OffsetX=0, OffsetY=0):
    return state.board.get((key[0] + OffsetX, key[1] + OffsetY))


def exists(state, key, OffsetX=0, OffsetY=0):
    return (key[0] + OffsetX, key[1] + OffsetY) in state.moves


def checkUpwardsDiagonal(state, key, problemPlayer, otherPlayer):
    if player(state, key) == problemPlayer:
        if player(state, key, 1, 1) == problemPlayer:
            if player(state, key, 2, 2) == problemPlayer:
                if player(state, key, 3, 3) == problemPlayer:
                    return float('inf')
                else:
                    return 35 if exists(state, key, 3, 3)else 0
            else:
                return 12 if exists(state, key, 2, 2) else 0
    else:
        if player(state, key, 1, 1) == otherPlayer:
            if player(state, key, 2, 2) == otherPlayer:
                if player(state, key, 3, 3) == otherPlayer:
                    return -float('inf')
                else:
                    return -35 if exists(state, key, 3, 3) else 0
            else:
                return -12 if exists(state, key, 2, 2) else 0
    return 0


def checkDownwardDiagonal(state, key, problemPlayer, otherPlayer):
    if player(state, key) == problemPlayer:
        if player(state, key, 1, -1) == problemPlayer:
            if player(state, key, 2, -2) == problemPlayer:
                if player(state, key, 3, -3) == problemPlayer:
                    return float('inf')
                else:
                    return 35 if exists(state, key, 3, -3) else 0
            else:
                return 12 if exists(state, key, 2, -2) else 0
    else:
        if player(state, key, 1, -1) == otherPlayer:
            if player(state, key, 2, -2) == otherPlayer:
                if player(state, key, 3, -3) == otherPlayer:
                    return -float('inf')
                else:
                    return -35 if exists(state, key, 3, -3) else 0
            else:
                return -12 if exists(state, key, 2, -2) else 0
    return 0


def heuristic(state, problemPlayer):
    heuristicValue = 0
    otherPlayer = "O" if problemPlayer == "X" else "X"
    for key in state.board:
        heuristicValue += VerticalHeuristic(state, problemPlayer, otherPlayer).heuristicIn(key)
        if heuristicValue == -float('inf') or heuristicValue == float('inf'):
            return heuristicValue
        heuristicValue += HorizontalHeuristic(state, problemPlayer, otherPlayer).heuristicIn(key)
        if heuristicValue == -float('inf') or heuristicValue == float('inf'):
            return heuristicValue
    return heuristicValue

        # heuristicsValue += checkDownwardDiagonal(state, key, problemPLayer, otherPlayer)
        #if heuristicValue == -float('inf') or heuristicValue == float('inf'):
            #return heuristicValue
        # heuristicsValue += checkUpwardsDiagonal(state, key, problemPLayer, otherPlayer)
        #if heuristicValue == -float('inf') or heuristicValue == float('inf'):
            #return heuristicValue

