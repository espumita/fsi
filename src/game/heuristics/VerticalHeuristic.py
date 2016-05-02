class VerticalHeuristic:

    def __init__(self, state, problemPlayer, otherPlayer):
        self.state = state
        self.problemPlayer = problemPlayer
        self.otherPlayer =otherPlayer

    def player(self, key, OffsetX=0, OffsetY=0):
        return self.state.board.get((key[0] + OffsetX, key[1] + OffsetY))

    def exists(self, key, OffsetX=0, OffsetY=0):
        return (key[0] + OffsetX, key[1] + OffsetY) in self.state.moves

    def heuristicIn(self, key):
        return self.checkProblemVerticalTwoConnectionExistence(key) if self.player(key) == self.problemPlayer else self.checkOtherVerticalTwoConnectionExistence(key)

    #Vertical problem

    def checkProblemVerticalTwoConnectionExistence(self, key):
        return 1 if self.exists(key, 0, 1) else self.checkProblemVerticalTwoConnection(key)

    def checkProblemVerticalTwoConnection(self, key):
        return self.checkProblemVerticalThreeConnectionExistence(key) if self.player(key, 0, 1) == self.problemPlayer else 0

    def checkProblemVerticalThreeConnectionExistence(self, key):
        return 5 if self.exists(key, 0, 2) else self.checkProblemVerticalThreeConnection(key)

    def checkProblemVerticalThreeConnection(self, key):
        return self.checkProblemVerticalFourConnectionExistence(key) if self.player(key, 0, 2) == self.problemPlayer else 0

    def checkProblemVerticalFourConnectionExistence(self, key):
        return 25 if self.exists(key, 0, 3) else self.checkProblemVerticalFourConnection(key)

    def checkProblemVerticalFourConnection(self, key):
        return float('inf') if self.player(key, 0, 3) == self.problemPlayer else 0

    #Vertical other
    
    def checkOtherVerticalTwoConnectionExistence(self, key):
        return -1 if self.exists(key, 0, 1) else self.checkOtherVerticalTwoConnection(key)

    def checkOtherVerticalTwoConnection(self, key):
        return self.checkOtherVerticalThreeConnectionExistence(key) if self.player(key, 0, 1) == self.otherPlayer else 0

    def checkOtherVerticalThreeConnectionExistence(self, key):
        return -5 if self.exists(key, 0, 2) else self.checkOtherVerticalThreeConnection(key)

    def checkOtherVerticalThreeConnection(self, key):
        return self.checkOtherVerticalFourConnectionExistence(key) if self.player(key, 0, 2) == self.otherPlayer else 0

    def checkOtherVerticalFourConnectionExistence(self, key):
        return -25 if self.exists(key, 0, 3) else self.checkOtherVerticalFourConnection(key)

    def checkOtherVerticalFourConnection(self, key):
        return -float('inf') if self.player(key, 0, 3) == self.otherPlayer else 0
