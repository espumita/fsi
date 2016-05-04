class HorizontalHeuristic:

    def __init__(self, state, problem_player, other_player):
        self.state = state
        self.problem_player = problem_player
        self.other_player =other_player

    def player(self, key, offset_x=0, offset_y=0):
        return self.state.board.get((key[0] + offset_x, key[1] + offset_y))

    def is_empty(self, key, offset_x=0, offset_y=0):
        return (key[0] + offset_x, key[1] + offset_y) in self.state.moves

    def heuristic(self):
        total_value = 0
        for line in range(1, 7):
            line_value = 0
            for column in range(1, 8):
                if not self.is_empty((column, line)):
                    if self.player((column, line)) == self.other_player:
                        return 0
                    else:
                        return 0



