def checkIfExistsAnotherSimilarTokenInColumn(state, key):
    for rowIndex in range(1,7):
        if rowIndex != key[0]:
            if state.board.get(rowIndex,key[1]) == state.to_move:
                return True
    return False


def checkSingleToken(state, key):
    accumulatedHeuristicsValue = 1
    if checkIfExistsAnotherSimilarTokenInColumn(state,key):
        accumulatedHeuristicsValue += 50
    return accumulatedHeuristicsValue

def firstHeuristics(state):
    heuristicsValue = 0
    for key in state.board:
        if state.board[key] == state.to_move:
                heuristicsValue += checkSingleToken(state, key)
    return heuristicsValue


