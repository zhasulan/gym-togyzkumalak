import gym
from gym import spaces

from gym_toguzkumalak.toguzkumalak.board import Board


class ToguzkumalakEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.__version__ = "0.0.1"

        self.action_space = spaces.Discrete(9)
        self.board = Board()

        pass

    def step(self, action):
        self.board.move(action=action)
        pass

    def reset(self):
        pass

    def render(self, mode='human'):
        pass
