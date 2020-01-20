import gym
from gym.spaces import Box
import numpy as np

from gym_togyzkumalak.envs.togyzkumalak_discrete import TogyzkumalakDiscrete
from gym_togyzkumalak.togyzkumalak.board import Board


class TogyzkumalakEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.__version__ = "0.0.1"

        self.board = Board()
        self.action_space = TogyzkumalakDiscrete(9, self.board)

        low = np.zeros((128, 1))
        high = np.ones((128, 1))

        for i in range(5, 56, 7):
            high[i] = 18
            pass
        high[61] = 18

        for i in range(63, 117, 7):
            high[i] = 18
            pass
        high[123] = 18

        self.observation_space = Box(low=low, high=high)

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

    def check_action(self, action):
        return self.board.run.check_action(action)

    def observation(self):
        return self.board.observation()

    def available_action(self):
        return self.board.run.available_action()

    def reward(self):
        return self.board.reward()
