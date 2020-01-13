This repository contains a PIP package which is an OpenAI environment for simulating an environment for Toguzkumalak game.

## Installation

Install the [OpenAI gym](https://gym.openai.com/docs/).

Then install this package via

```
pip install -e .
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