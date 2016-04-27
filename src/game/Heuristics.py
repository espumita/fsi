def checkVerticalConnection(state, key):
    if state.board.get((key[0], key[1])) == "X":
        if state.board.get((key[0], key[1]+1)) == "X":
            if state.board.get((key[0], key[1]+2)) == "X":
                if state.board.get((key[0], key[1]+3)) == "X":
                    return float('inf')
                else:
                    return 10
            else:
                return 5
    else:
        if state.board.get((key[0], key[1]+1)) == "O":
            if state.board.get((key[0], key[1]+2)) == "O":
                if state.board.get((key[0], key[1]+3)) == "O":
                    return -float('inf')
                else:
                    return -10
            else:
                return -5
    return 0

def checkHorizontalConnection(state, key):
    if state.board.get((key[0], key[1])) == "X":
        if state.board.get((key[0]+1, key[1])) == "X":
            if state.board.get((key[0]+2, key[1])) == "X":
                if state.board.get((key[0]+3, key[1])) == "X":
                    return float('inf')
                else:
                    return 10
            else:
                return 5
    else:
        if state.board.get((key[0]+1, key[1])) == "O":
            if state.board.get((key[0]+2, key[1])) == "O":
                if state.board.get((key[0]+3, key[1])) == "O":
                    return -float('inf')
                else:
                    return -10
            else:
                return -5
    return 0

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


