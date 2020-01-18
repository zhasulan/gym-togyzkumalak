<h1 align="center">Toguzkumalak OpenAI Gym</h1> <br>
<p align="center">
   <img alt="Toguzkumalak" title="Toguzkumalak" src="./logo.jpg" width="350">
</p>

# Table of Contents
- [About Game](#about_game)
- [gym-toguzkumalak](#gym_toguzkumalak)
- [Installation](#installation)
- [Environment](#env)
    - [Observation](#observation)
    - [Actions](#actions)
    - [Reward](#reward)
    - [Starting State](#starting_state)
    - [Episode Termination](#episode_termination)
    - [Reset](#reset)
    - [Rendering](#rendering)
    - [Example](#example)
        - [Play random Agents](#play)
        - [Valid actions](#valid_actions)
- [Useful links and related works](#useful_links)
- [License](#license)

---
## <a name="about_game"></a>About Game
Toguz Kumalak (тоғыз құмалақ - Kazakh for “sheep droppings”), also known as Toguz Korgool (тогуз коргоол; same meaning) in Kyrgyz, is widely played in Central Asia. It is one of the few mancala games in which pits can be captured and turned into accumulation holes, a distinctive feature that adds another layer of strategic complexity. Toguz Kumalak has become a major mind sport that is officially promoted by the governments of Kazakhstan and Kyrgyztan.

---
## <a name="gym_toguzkumalak"></a>gym-toguzkumalak
This repository contains a PIP package which is an OpenAI environment for simulating an environment for Toguzkumalak game.

## <a name="installation"></a>Installation

Install the [OpenAI gym](https://gym.openai.com/docs/).

Then install this package via

```
git clone https://github.com/zhasulan/gym-toguzkumalak.git
cd gym-toguzkumalak/
pip install -e .
```
or
```
pip install gym-toguzkumalak
```

---
## <a name="env"></a>Environment
The encoding used to represent the state is inspired by the one used by Gerald Tesauro[1].

## Usage

```
import gym
import gym_toguzkumalak

env = gym.make('Toguzkumalak-v0')
```

See https://github.com/matthiasplappert/keras-rl/tree/master/examples for some
examples.

---
## <a name="useful_links"></a>Useful links

- [https://www.abstractgames.org/toguz-kumalak.html](https://www.abstractgames.org/toguz-kumalak.html)
- [Wikipedia](https://en.wikipedia.org/wiki/Toguz_korgol)

---
## <a name="license"></a>License
[MIT](https://github.com/dellalibera/gym-backgammon/blob/master/LICENSE) 