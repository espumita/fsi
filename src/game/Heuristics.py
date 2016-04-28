def checkVerticalConnection(state, key):
    if state.board.get((key[0], key[1])) == "X":
        if state.board.get((key[0], key[1]+1)) == "X":
            if state.board.get((key[0], key[1]+2)) == "X":
                if state.board.get((key[0], key[1]+3)) == "X":
                    return float('inf')
                else:
                    if (key[0],key[1]+3) in state.moves:
                        return 25
                    else:
                        return 0
            else:
                if (key[0],key[1]+2) in state.moves:
                    return 5
                else:
                    return 0
    else:
        if state.board.get((key[0], key[1]+1)) == "O":
            if state.board.get((key[0], key[1]+2)) == "O":
                if state.board.get((key[0], key[1]+3)) == "O":
                    return -float('inf')
                else:
                    if (key[0],key[1]+3) in state.moves:
                        return -25
                    else:
                        return 0
            else:
                if (key[0],key[1]+2) in state.moves:
                    return -5
                else:
                    return 0
    return 0

def checkHorizontalConnection(state, key):
    if state.board.get((key[0], key[1])) == "X":
        if state.board.get((key[0]+1, key[1])) == "X":
            if state.board.get((key[0]+2, key[1])) == "X":
                if state.board.get((key[0]+3, key[1])) == "X":
                    return float('inf')
                else:
                    if (key[0]+3,key[1]) in state.moves:
                        return 30
                    else:
                        return 0
            else:
                if (key[0]+2,key[1]) in state.moves:
                    return 8
                else:
                    return 0
    else:
        if state.board.get((key[0]+1, key[1])) == "O":
            if state.board.get((key[0]+2, key[1])) == "O":
                if state.board.get((key[0]+3, key[1])) == "O":
                    return -float('inf')
                else:
                    if (key[0]+3,key[1]) in state.moves:
                        return -30
                    else:
                        return 0
            else:
                if (key[0]+2,key[1]) in state.moves:
                    return -8
                else:
                    return 0
    return 0


def checkUpwardsDiagonal(state, key):
    if state.board.get((key[0], key[1])) == "X":
        if state.board.get((key[0]+1, key[1]+1)) == "X":
            if state.board.get((key[0]+2, key[1]+2)) == "X":
                if state.board.get((key[0]+3, key[1]+3)) == "X":
                    return float('inf')
                else:
                    if (key[0]+3,key[1]+3) in state.moves:
                        return 45
                    else:
                        return 0
            else:
                if (key[0]+2,key[1]+2) in state.moves:
                    return 12
                else:
                    return 0
    else:
        if state.board.get((key[0]+1, key[1]+1)) == "O":
            if state.board.get((key[0]+2, key[1]+2)) == "O":
                if state.board.get((key[0]+3, key[1]+3)) == "O":
                    return -float('inf')
                else:
                    if (key[0]+3,key[1]+3) in state.moves:
                        return -45
                    else:
                        return 0
            else:
                if (key[0]+2,key[1]+2) in state.moves:
                    return -12
                else:
                    return 0
    return 0


def checkDownwardDiagonal(state, key):
    if state.board.get((key[0], key[1])) == "X":
        if state.board.get((key[0]+1, key[1]-1)) == "X":
            if state.board.get((key[0]+2, key[1]-2)) == "X":
                if state.board.get((key[0]+3, key[1]-3)) == "X":
                    return float('inf')
                else:
                    if (key[0]+3,key[1]-3) in state.moves:
                        return 45
                    else:
                        return 0
            else:
                if (key[0]+2,key[1]-2) in state.moves:
                    return 12
                else:
                    return 0
    else:
        if state.board.get((key[0]+1, key[1]-1)) == "O":
            if state.board.get((key[0]+2, key[1]-2)) == "O":
                if state.board.get((key[0]+3, key[1]-3)) == "O":
                    return -float('inf')
                else:
                    if (key[0]+3,key[1]-3) in state.moves:
                        return -45
                    else:
                        return 0
            else:
                if (key[0]+2,key[1]-2) in state.moves:
                    return -12
                else:
                    return 0
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
        #heuristicsValue += checkUpwardsDiagonal(state, key)
        if heuristicsValue == -float('inf'):
            return -float('inf')
        if heuristicsValue == float('inf'):
            return float('inf')
        #heuristicsValue += checkDownwardDiagonal(state, key)
        if heuristicsValue == -float('inf'):
            return -float('inf')
        if heuristicsValue == float('inf'):
            return float('inf')
    return heuristicsValue


