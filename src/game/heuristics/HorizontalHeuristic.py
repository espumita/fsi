class HorizontalHeuristic:

    def __init__(self, state, problemPlayer, otherPlayer):
        self.state = state
        self.problemPlayer = problemPlayer
        self.otherPlayer =otherPlayer

    def player(self, key, OffsetX=0, OffsetY=0):
        return self.state.board.get((key[0] + OffsetX, key[1] + OffsetY))

    def exists(self, key, OffsetX=0, OffsetY=0):
        return (key[0] + OffsetX, key[1] + OffsetY) in self.state.moves

    def heuristicIn(self, key):
        return self.checkProblemHorizontalTwoConnectionExistence(key) if self.player(key) == self.problemPlayer else self.checkOtherHorizontalTwoConnectionExistence(key)

    #Horizontal problem
    def checkProblemHorizontalTwoConnectionExistence(self, key):
        return 1 if self.exists(key, 1) else 0

    #Horizontal other
    def checkOtherHorizontalTwoConnectionExistence(self, key):
        return -1 if self.exists(key, 1) else 0
