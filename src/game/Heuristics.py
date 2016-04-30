def player(state, key, OffsetX=0, OffsetY=0):
    return state.board.get((key[0] + OffsetX, key[1] + OffsetY))


def exists(state, key, OffsetX=0, OffsetY=0):
    return (key[0] + OffsetX, key[1] + OffsetY) in state.moves


def checkVerticalConnection(state, key, problemPlayer, otherPlayer):
    if player(state, key) == problemPlayer:
        if player(state, key, 0, 1) == problemPlayer:
            if player(state, key, 0, 2) == problemPlayer:
                if player(state, key, 0, 3) == problemPlayer:
                    return float('inf')
                else:
                    return 25 if exists(state, key, 0, 3) else 0
            else:
                return 5 if exists(state, key, 0, 2) else 0
        else:
            return 1
    else:
        if player(state, key, 0, 1) == otherPlayer:
            if player(state, key, 0, 2) == otherPlayer:
                if player(state, key, 0, 3) == otherPlayer:
                    return -float('inf')
                else:
                    return -25 if exists(state, key, 0, 3) else 0
            else:
                return -5 if exists(state, key, 0, 2) else 0
        else:
            return -1
    return 0


def checkHorizontalConnection(state, key, problemPlayer, otherPlayer):
    if player(state, key) == problemPlayer:
        if player(state, key, 1) == problemPlayer:
            if player(state, key, 2) == problemPlayer:
                if player(state, key, 3) == problemPlayer:
                    return float('inf')
                else:
                    return 30 if exists(state, key, 3) else 0
            else:
                return 8 if exists(state, key, 2) else 0
    else:
        if player(state, key, 1) == otherPlayer:
            if player(state, key, 2) == otherPlayer:
                if player(state, key, 3) == otherPlayer:
                    return -float('inf')
                else:
                    return -30 if exists(state, key, 3) else 0
            else:
                return -8 if exists(state, key, 2) else 0
    return 0


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


def firstHeuristics(state, problemPlayer):
    heuristicsValue = 0
    otherPlayer = "O" if problemPlayer == "X" else "X"
    for key in state.board:
        heuristicsValue += checkVerticalConnection(state, key, problemPlayer, otherPlayer)
        if heuristicsValue == -float('inf') or heuristicsValue == float('inf'):
            return heuristicsValue
        #heuristicsValue += checkHorizontalConnection(state, key, problemPlayer, otherPlayer)
        if heuristicsValue == -float('inf') or heuristicsValue == float('inf'):
            return heuristicsValue
        # heuristicsValue += checkDownwardDiagonal(state, key, problemPLayer, otherPlayer)
        if heuristicsValue == -float('inf') or heuristicsValue == float('inf'):
            return heuristicsValue
        # heuristicsValue += checkUpwardsDiagonal(state, key, problemPLayer, otherPlayer)
        if heuristicsValue == -float('inf') or heuristicsValue == float('inf'):
            return heuristicsValue
    return heuristicsValue
