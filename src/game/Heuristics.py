
def checkPerimeter(state,key):
    value = 0
    if state.board.get((key[0]-1,key[1])) != None:
        if state.board.get((key[0]-1,key[1])) == "X":
            value += 5
        else:
            value += -3
    if state.board.get((key[0]+1,key[1])) != None:
        if state.board.get((key[0]+1,key[1])) == "X":
            value += 5
        else:
            value += -3
    if state.board.get((key[0],key[1]-1)) != None:
        if state.board.get((key[0],key[1]-1)) == "X":
            value += 5
        else:
            value += -3
    if state.board.get((key[0],key[1]+1)) != None:
        if state.board.get((key[0],key[1]+1)) == "X":
            value += 5
        else:
            value += -3
    if state.board.get((key[0]-1,key[1]+1)) != None:
        if state.board.get((key[0]-1,key[1]+1)) == "X":
            value += 10
        else:
            value += -6
    if state.board.get((key[0]+1,key[1]-1)) != None:
        if state.board.get((key[0]+1,key[1]-1)) == "X":
            value += 10
        else:
            value += -6
    if state.board.get((key[0]+1,key[1]+1)) != None:
        if state.board.get((key[0]+1,key[1]+1)) == "X":
            value += 10
        else:
            value += -6
    if state.board.get((key[0]-1,key[1]-1)) != None:
        if state.board.get((key[0]-1,key[1]-1)) == "X":
            value += 10
        else:
            value += -6
    return value

def firstHeuristics(state):
    heuristicsValue = 0
    for key in state.board:
        if state.board[key] == "X":
            #heuristicsValue += checkPerimeter(state,key)
            return checkPerimeter(state,key)
