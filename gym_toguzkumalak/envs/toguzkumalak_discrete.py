from gym.spaces import Discrete


class ToguzkumalakDiscrete(Discrete):

    def __init__(self, n, board):
        super(ToguzkumalakDiscrete, self).__init__(n)
        self.board = board
        pass

    def update_board(self, board):
        self.board = board

    def sample(self):
        return self.board.sample_action()
