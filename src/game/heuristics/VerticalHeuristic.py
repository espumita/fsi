class VerticalHeuristic:

    def __init__(self, state, problemPlayer, otherPlayer):
        self.state = state
        self.problemPlayer = problemPlayer
        self.otherPlayer = otherPlayer

    def player(self, key, OffsetX=0, OffsetY=0):
        return self.state.board.get((key[0] + OffsetX, key[1] + OffsetY))

    def isEmpty(self, key, OffsetX=0, OffsetY=0):
        return (key[0] + OffsetX, key[1] + OffsetY) in self.state.moves

    def heuristic(self):
        totalValue = 0
        for column in range(1, 8):
            columnValue = 0
            for line in range(1, 7):
                if self.isEmpty((column, line)):
                    break
                if self.player((column, line)) == "X":
                    if self.isEmpty((column, line), 0, 1):
                        columnValue += 10
                    else:
                        if self.player((column, line), 0, 1) == "X":
                            columnValue += 240
                            if columnValue >= 700:
                                return float('inf')
                        else:
                            columnValue = 1
                else:
                    if self.player((column, line)) == "O":
                        if self.isEmpty((column, line), 0, 1):
                            columnValue -= 10
                        else:
                            if self.player((column, line), 0, 1) == "O":
                                columnValue -= 240
                                if columnValue <= -700:
                                    return -float('inf')
                            else:
                                columnValue = 0
            totalValue += columnValue
        return totalValue
