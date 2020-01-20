import gym
import gym_togyzkumalak


def main():
    env = gym.make('Togyzkumalak-v0')
    env.reset()

    done = False
    state, reward = None, None

    while not done:
        state, reward, done, info = env.step(env.action_space.sample())
        env.render()
        pass

    print(state.shape, reward)
    pass


if __name__ == '__main__':
    main()
