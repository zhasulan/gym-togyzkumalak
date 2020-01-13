This repository contains a PIP package which is an OpenAI environment for simulating an environment for Toguzkumalak game.

## Installation

Install the [OpenAI gym](https://gym.openai.com/docs/).

Then install this package via

```
pip install -e .
```

or

```
pip install gym-toguzkumalak
```

## Usage

```
import gym
import gym_toguzkumalak

env = gym.make('Toguzkumalak-v0')
```

See https://github.com/matthiasplappert/keras-rl/tree/master/examples for some
examples.


## The Environment

The environment provides old central Asia game [Toguzkumalak](https://en.wikipedia.org/wiki/Toguz_korgol). This is one of the variant of game of [Mancala](https://en.wikipedia.org/wiki/Mancala). The toguzkumalak is a family of two-player turn-based strategy board game.
Environment of this game provide full information. 