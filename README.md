<h1 align="center">Toguzkumalak OpenAI Gym</h1> <br>
<p align="center">
   <img alt="Toguzkumalak" title="Toguzkumalak" src="./logo.jpg" width="350">
</p>

# Table of Contents
- [About Game](#about_game)
- [Rules](#rules)
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
## <a name="rules"></a>Rules
The game is played on a board, which consists of two rows of nine oblong holes (otau, literally, “yurt”) and two parallel furrows (kazan, literally, “kettle”) between them. The kazan serve as stores for captured balls. Initially, there are 9 little black balls (kumalak) in each hole. The holes are made in such a way that the two players can easily distinguish between an odd and an even number of balls. In addition, each player has a larger ball in a different color (usually white) that serves as a marker for any tuzduk the player might make later (see below). The players sit opposite each other, on the long sides of the board, directly in front of their holes. A player’s kazan, however, is adjacent to the opponent’s row. The player who starts the game is called “White”, the other player “Black”.
Picture
Toguz Kumalak starting position. White is light blue; Black is dark blue.
At his turn, a player takes with his index and middle finger all the balls of one of his holes, except one ball that is left in the hole, and distributes them, one by one, into the following holes in an anticlockwise direction around the board. If a hole contains only one ball, it is put into the next hole.

If the last ball thus sown makes the contents of an opponent’s hole even, its contents are captured. They are shifted with the index and the middle finger into the player’s kazan. Note that the opening move of each game captures 10 balls except move 19 (see notation), which is for that reason a bad move.

If the last ball falls into an opponent’s hole that has two balls (then numbering three balls), this hole is turned into a tuzduk (literally, “salty”) and marked with a special ball. During the game any balls, which fall into a tuzduk, are won by the player who owns the tuzduk, and are then transferred into this player’s kazan. A tuzduk is never skipped. Therefore, a tuzduk is an acquired accumulation hole, quite similar to the lubang rumah in Congkak or the kalah in the game of Kalah (usually known as “mancala” in the USA), except that in these games the accumulation holes are fixed from the beginning.

There are some restrictions in regard to the tuzduk:

Each player can create a tuzduk only once in a game. Players are permitted to make more moves that end in enemy holes containing two balls, but they will not turn them into tuzduk’s.
The ninth hole of the opponent cannot be turned into a tuzduk, only holes 1-8.
A hole becomes immune from being turned into a tuzduk, when the corresponding hole of the opponent has already become a tuzduk. For instance, if your opponent has created his tuzduk in YOUR second hole, you are no longer able to make a tuzduk in HIS second hole.

The players move alternately and passing is prohibited. The game is finished when a player, on his turn, cannot make a move. In Kazakh this is called atsis kalu (literally, “left without a horse”). A player owns the balls he captured, the balls which fell into his tuzduk, and those that are still in his holes. The player with 82 balls or more wins. If both players have 81 balls, the game is a draw. In practical play, the game ends as soon as one player has secured the minimum number of balls needed to win, and the remaining moves are not played out.

Game clocks are used in all important Toguz Kumalak tournaments. In world championships the thinking time is up to three hours for each player. In blitz tournaments, however, players may be given as little as seven minutes. When a player’s time has expired, the balls that have not been captured yet are awarded to his opponent.

---
## <a name="gym_toguzkumalak"></a>gym-toguzkumalak
This repository contains a Toguz Kumalak game implementation in OpenAI Gym.
Given the current state of the board, and the current player, it computes all the legal actions/moves (iteratively) that the current player can execute. The legal actions are generated in such a way that they can be moved in comparison with other actions that cannot be moved due to the fact that the holes may be empty or they are in a tuzduk state.

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