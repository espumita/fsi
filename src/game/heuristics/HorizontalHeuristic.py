class HorizontalHeuristic:

    def __init__(self, state, problem_player, other_player):
        self.state = state
        self.problem_player = problem_player
        self.other_player = other_player

    def heuristic(self):
        total_value = 0
        for line in range(1, 7):
            line_value = 0
            for column in range(1, 8):
                if not self.is_empty((column, line)):
                    if self.player((column, line)) == self.problem_player:
                        if self.player((column, line), -1) == self.problem_player:
                            pass
                        else:
                            offset = 1
                            while self.player((column, line), offset) == self.problem_player:
                                offset += 1
                            if offset >= 4:
                                return float('inf')
                            if offset == 3:
                                if self.is_empty((column, line), offset):
                                    if self.is_empty((column, line), -1):
                                        line_value = 590
                                    else:
                                        if self.player((column, line), -1) == self.other_player:
                                            line_value = 500
                                else:
                                    if self.player((column, line), offset) == self.other_player:
                                        if self.is_empty((column, line), -1):
                                            line_value = 500
                                        else:
                                            line_value = 0
                            if offset == 2:
                                if self.is_empty((column, line), offset):
                                    if self.is_empty((column, line), -1):
                                        line_value = 340
                                    else:
                                        if self.player((column, line), -1) == self.other_player:
                                            line_value = 300
                                else:
                                    if self.player((column, line), offset) == self.other_player:
                                        if self.is_empty((column, line), -1):
                                            line_value = 300
                                        else:
                                            line_value = 0
                            if offset == 1:
                                if self.is_empty((column, line), offset):
                                    if self.is_empty((column, line), -1):
                                        line_value = 40
                                    else:
                                        if self.player((column, line), -1) == self.other_player:
                                            line_value = 20
                                else:
                                    if self.player((column, line), offset) == self.other_player:
                                        if self.is_empty((column, line), -1):
                                            line_value = 20
                                        else:
                                            line_value = 0
                    else:
                        if self.player((column, line), -1) == self.other_player:
                            pass
                        else:
                            offset = 1
                            while self.player((column, line), offset) == self.other_player:
                                offset += 1
                            if offset >= 4:
                                return -float('inf')
                            if offset == 3:
                                if self.is_empty((column, line), offset):
                                    if self.is_empty((column, line), -1):
                                        line_value = -590
                                    else:
                                        if self.player((column, line), -1) == self.problem_player:
                                            line_value = -500
                                else:
                                    if self.player((column, line), offset) == self.problem_player:
                                        if self.is_empty((column, line), -1):
                                            line_value = -500
                                        else:
                                            line_value = 0
                            if offset == 2:
                                if self.is_empty((column, line), offset):
                                    if self.is_empty((column, line), -1):
                                        line_value = -340
                                    else:
                                        if self.player((column, line), -1) == self.problem_player:
                                            line_value = -300
                                else:
                                    if self.player((column, line), offset) == self.problem_player:
                                        if self.is_empty((column, line), -1):
                                            line_value = -300
                                        else:
                                            line_value = 0
                            if offset == 1:
                                if self.is_empty((column, line), offset):
                                    if self.is_empty((column, line), -1):
                                        line_value = -40
                                    else:
                                        if self.player((column, line), -1) == self.problem_player:
                                            line_value = -20
                                else:
                                    if self.player((column, line), offset) == self.problem_player:
                                        if self.is_empty((column, line), -1):
                                            line_value = -20
                                        else:
                                            line_value = 0

            total_value += line_value
        return total_value

    def player(self, key, offset_x=0, offset_y=0):
        return self.state.board.get((key[0] + offset_x, key[1] + offset_y))

    def is_empty(self, key, offset_x=0, offset_y=0):
        return (key[0] + offset_x, key[1] + offset_y) in self.state.moves

