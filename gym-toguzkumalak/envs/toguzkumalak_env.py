import gym

from toguzkumalak.board import Board


class ToguzkumalakEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.board = Board()
        pass

    def step(self, action):
        self.board.move(action=action)
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass
