import gym
from gym.spaces import Box
import numpy as np

from gym_toguzkumalak.envs.toguzkumalak_discrete import ToguzkumalakDiscrete
from gym_toguzkumalak.toguzkumalak.board import Board


class ToguzkumalakEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.__version__ = "0.0.6"

        self.board = Board()
        self.action_space = ToguzkumalakDiscrete(9, self.board)
        self.observation_space = Box(0, 162, shape=(38,), dtype=np.int)

        pass

    def step(self, action):
        observation, reward, done, info = self.board.move(action=action)
        self.action_space.update_board(self.board)
        return observation, reward, done, info

    def reset(self):
        self.board = Board()
        self.action_space.update_board(self.board)
        return self.board.observation()

    def render(self, mode='human'):
        self.board.print()
        pass
