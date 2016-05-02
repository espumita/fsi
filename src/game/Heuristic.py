
def player(state, key, OffsetX=0, OffsetY=0):
    return state.board.get((key[0] + OffsetX, key[1] + OffsetY))


def exists(state, key, OffsetX=0, OffsetY=0):
    return (key[0] + OffsetX, key[1] + OffsetY) in state.moves


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


def heuristic(state, problemPlayer):
    heuristicValue = 0
    otherPlayer = "O" if problemPlayer == "X" else "X"
    for key in state.board:
        heuristicValue += checkProblemVerticalTwoConnectionExistence(state, key, problemPlayer) if player(state, key) == problemPlayer else checkOtherVerticalTwoConnectionExistence(state, key, otherPlayer)
    return heuristicValue

        #heuristicValue += checkVerticalConnection(state, key, problemPlayer, otherPlayer)
        #if heuristicValue == -float('inf') or heuristicValue == float('inf'):
            #return heuristicValue
        # heuristicsValue += checkHorizontalConnection(state, key, problemPlayer, otherPlayer)
        #if heuristicValue == -float('inf') or heuristicValue == float('inf'):
            #return heuristicValue
        # heuristicsValue += checkDownwardDiagonal(state, key, problemPLayer, otherPlayer)
        #if heuristicValue == -float('inf') or heuristicValue == float('inf'):
            #return heuristicValue
        # heuristicsValue += checkUpwardsDiagonal(state, key, problemPLayer, otherPlayer)
        #if heuristicValue == -float('inf') or heuristicValue == float('inf'):
            #return heuristicValue


def checkProblemVerticalTwoConnectionExistence(state, key, problemPlayer):
    return 1 if exists(state, key, 0, 1) else checkProblemVerticalTwoConnection(key, problemPlayer, state)


def checkProblemVerticalTwoConnection(key, problemPlayer, state):
    return checkProblemVerticalThreeConnectionExistence(state, key, problemPlayer) if player(state, key, 0, 1) == problemPlayer else 0


def checkProblemVerticalThreeConnectionExistence(state, key, problemPlayer):
    return 5 if exists(state, key, 0, 2) else checkProblemVerticalThreeConnection(state, key, problemPlayer)


def checkProblemVerticalThreeConnection(state, key, problemPlayer):
    return checkProblemVerticalFourConnectionExistence(state, key, problemPlayer) if player(state, key, 0, 2) == problemPlayer else 0


def checkProblemVerticalFourConnectionExistence(state, key, problemPlayer):
    return 25 if exists(state, key, 0, 3) else checkProblemVerticalFourConnection(state, key, problemPlayer)


def checkProblemVerticalFourConnection(state, key, problemPlayer):
    return float('inf') if player(state, key, 0, 3) == problemPlayer else 0







def checkOtherVerticalTwoConnectionExistence(state, key, otherPlayer):
    return -1 if exists(state, key, 0, 1) else checkOtherVerticalTwoConnection(state, key, otherPlayer)


def checkOtherVerticalTwoConnection(state, key, otherPlayer):
    return checkOtherVerticalThreeConnectionExistence(state, key, otherPlayer) if player(state, key, 0, 1) == otherPlayer else 0


def checkOtherVerticalThreeConnectionExistence(state, key, otherPlayer):
    return -5 if exists(state, key, 0, 2) else checkOtherVerticalThreeConnection(state, key, otherPlayer)


def checkOtherVerticalThreeConnection(state, key, otherPlayer):
    return checkOtherVerticalFourConnectionExistence(state, key, otherPlayer) if player(state, key, 0, 2) == otherPlayer else 0


def checkOtherVerticalFourConnectionExistence(state, key, otherPlayer):
    return -25 if exists(state, key, 0, 3) else checkOtherVerticalFourConnection(state, key, otherPlayer)


def checkOtherVerticalFourConnection(state, key, otherPlayer):
    return -float('inf') if player(state, key, 0, 3) == otherPlayer else 0
