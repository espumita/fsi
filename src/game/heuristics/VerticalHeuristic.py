class VerticalHeuristic:

    def __init__(self, state, problemPlayer, otherPlayer):
        self.state = state
        self.problemPlayer = problemPlayer
        self.otherPlayer = otherPlayer

    def player(self, key, OffsetX=0, OffsetY=0):
        return self.state.board.get((key[0] + OffsetX, key[1] + OffsetY))

    def isEmpty(self, key, OffsetX=0, OffsetY=0):
        return (key[0] + OffsetX, key[1] + OffsetY) in self.state.moves

    def heuristicIn(self):
        value = 0
        for column in (1, 8):
            result = 0
            for line in (1, 7):
                if self.player((column, line)) == "X":
                    if self.isEmpty((column, line), 0, 1):
                        result += 10
                    else:
                        if self.player((column, line), 0, 1) == "X":
                            result += 250
                            if result >= 750:
                                return float('inf')
                        else:
                            result = 0

                if self.player((column, line)) == "O":
                    if self.isEmpty((column, line), 0, 1):
                        result -= 10
                    else:
                        if self.player((column, line), 0, 1) == "O":
                            result -= 250
                            if result <= -750:
                                return -float('inf')
                        else:
                            result = 0
            value += result
        return value
