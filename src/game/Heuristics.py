def checkVerticalConnection(state, key):
    accumulatedValue = 0
    if state.board.get((key[0], key[1])) == "X":
        if state.board.get((key[0], key[1]+1)) == "X":
            accumulatedValue += 5
            if state.board.get((key[0], key[1]+2)) == "X":
                accumulatedValue += 10
                if state.board.get((key[0], key[1]+3)) == "X":
                    return float('inf')
                else:
                    accumulatedValue = 4
            else:
                accumulatedValue = 14
    else:
        if state.board.get((key[0], key[1]+1)) == "O":
            accumulatedValue -= 5
            if state.board.get((key[0], key[1]+2)) == "O":
                accumulatedValue -= 10
                if state.board.get((key[0], key[1]+3)) == "O":
                    return -float('inf')
                else:
                    accumulatedValue = 4
            else:
                accumulatedValue = 14
    return accumulatedValue


def checkHorizontalConnection(state, key):
    accumulatedValue = 0
    if state.board.get((key[0], key[1])) == "X":
        if state.board.get((key[0]+1, key[1])) == "X":
            accumulatedValue += 5
            if state.board.get((key[0]+2, key[1])) == "X":
                accumulatedValue += 10
                if state.board.get((key[0]+3, key[1])) == "X":
                    return float('inf')
                else:
                    accumulatedValue = 4
            else:
                accumulatedValue = 14
    else:
        if state.board.get((key[0]+1, key[1])) == "O":
            accumulatedValue -= 5
            if state.board.get((key[0]+2, key[1])) == "O":
                accumulatedValue -= 10
                if state.board.get((key[0]+3, key[1])) == "O":
                    return -float('inf')
                else:
                    accumulatedValue = 4
            else:
                accumulatedValue = 14
    return accumulatedValue


def firstHeuristics(state):
    heuristicsValue = 0
    for key in state.board:
        heuristicsValue += checkVerticalConnection(state, key)
        if heuristicsValue == -float('inf'):
            return -float('inf')
        if heuristicsValue == float('inf'):
            return float('inf')
        heuristicsValue += checkHorizontalConnection(state, key)
        if heuristicsValue == -float('inf'):
            return -float('inf')
        if heuristicsValue == float('inf'):
            return float('inf')
    return heuristicsValue


