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
        return 1 if self.exists(key, 1) else self.checkProblemHorizontalTwoConnection(key)

    def checkProblemHorizontalTwoConnection(self, key):
        return self.checkProblemHorizontalThreeConnectionExistence(key) if self.player(key, 1) == self.problemPlayer else 0

    def checkProblemHorizontalThreeConnectionExistence(self, key):
        return 8 if self.exists(key, 2) else self.checkProblemHorizontalThreeConnection(key)

    def checkProblemHorizontalThreeConnection(self, key):
        return self.checkProblemHorizontalFourConnectionExistence(key) if self.player(key, 2) == self.problemPlayer else 0

    def checkProblemHorizontalFourConnectionExistence(self, key):
        return 30 if self.exists(key, 3) else self.checkProblemHorizontalFourConnection(key)

    def checkProblemHorizontalFourConnection(self, key):
        return float('inf') if self.player(key, 3) == self.problemPlayer else 0

    #Horizontal other

    def checkOtherHorizontalTwoConnectionExistence(self, key):
        return -1 if self.exists(key, 1) else self.checkOtherHorizontalTwoConnection(key)

    def checkOtherHorizontalTwoConnection(self, key):
        return self.checkOtherHorizontalThreeConnectionExistence(key) if self.player(key, 1) == self.otherPlayer else 0

    def checkOtherHorizontalThreeConnectionExistence(self, key):
        return -8 if self.exists(key, 2) else self.checkOtherHorizontalThreeConnection(key)

    def checkOtherHorizontalThreeConnection(self, key):
        return self.checkOtherHorizontalFourConnectionExistence(key) if self.player(key, 2) == self.otherPlayer else 0

    def checkOtherHorizontalFourConnectionExistence(self, key):
        return -30 if self.exists(key, 3) else self.checkOtherHorizontalFourConnection(key)

    def checkOtherHorizontalFourConnection(self, key):
        return -float('inf') if self.player(key, 3) == self.otherPlayer else 0

