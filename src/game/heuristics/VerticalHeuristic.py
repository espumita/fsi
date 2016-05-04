class VerticalHeuristic:

    def __init__(self, state, problem_player, other_player):
        self.state = state
        self.problem_player = problem_player
        self.other_player = other_player

    def heuristic(self):
        total_value = 0
        for column in range(1, 8):
            column_value = 0
            for line in range(1, 7):
                if self.is_empty((column, line)):
                    break
                if self.player((column, line)) == self.problem_player:
                    if self.is_empty((column, line), 0, 1):
                        column_value += 10
                    else:
                        if self.player((column, line), 0, 1) == self.problem_player:
                            column_value += 240
                            if column_value >= 700:
                                return float('inf')
                        else:
                            column_value = 1
                else:
                    if self.player((column, line)) == self.other_player:
                        if self.is_empty((column, line), 0, 1):
                            column_value -= 10
                        else:
                            if self.player((column, line), 0, 1) == self.other_player:
                                column_value -= 240
                                if column_value <= -700:
                                    return -float('inf')
                            else:
                                column_value = 0
            total_value += column_value
        return total_value

    def player(self, key, offset_x=0, offset_y=0):
        return self.state.board.get((key[0] + offset_x, key[1] + offset_y))

    def is_empty(self, key, offset_x=0, offset_y=0):
        return (key[0] + offset_x, key[1] + offset_y) in self.state.moves
