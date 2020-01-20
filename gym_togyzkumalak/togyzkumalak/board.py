import texttable

from gym_togyzkumalak.togyzkumalak.gamer import Gamer
from gym_togyzkumalak.togyzkumalak.kazan import Kazan

import numpy as np

from gym_togyzkumalak.togyzkumalak.otau import Otau


class Board:

    def __init__(self):
        self.reward = 0
        self.gamers = {
            'white': Gamer('white'),
            'black': Gamer('black')
        }

        self.run: Gamer = self.gamers['white']
        self.opponent: Gamer = self.gamers['black']

    def opponent_gamer(self, gamer: Gamer) -> Gamer:
        return self.gamers['white'] if gamer.name == 'black' else self.gamers['black']

    def switch_gamer(self):
        opponent: Gamer = self.run
        self.run = self.gamers['white'] if self.run.name == 'black' else self.gamers['black']
        self.opponent = opponent
        pass

    def switch_home(self, current_gamer_home):
        return self.gamers[current_gamer_home.name].home

    def win_gamer(self, gamer: Gamer):
        if gamer.name == 'white':
            self.reward = 1
            pass
        else:
            self.reward = -1
        pass

    def sample_action(self):
        try:
            return self.run.sample_action()
        except IndexError:
            self.win_gamer(self.opponent)
            raise Exception("Более отстутствуют ходы")
        pass

    # def predict_actions_state(self):
    #     for i in range(9):
    #         self.run.home[]

    def observation(self):
        if self.run.name == 'white':
            return np.array(self.run.observation(self.opponent.kazan) + self.opponent.observation(self.run.kazan) + [1, 0])
        else:
            return np.array(self.opponent.observation(self.run.kazan) + self.run.observation(self.opponent.kazan) + [0, 1])

        # if self.run.name == 'white':
        #     return np.array(self.run.observation() + self.opponent.observation())
        # else:
        #     return np.array(self.opponent.observation() + self.run.observation())
        # return [np.array(self.run.observation() + self.opponent.observation()), np.array(self.opponent.observation() + self.run.observation())]

    # def reward(self):
    #     return self.run.reward
        # return np.array([self.run.reward, self.opponent.reward])

    def take(self, otau: Otau):
        self.run.add(otau.kumalaks)
        otau.taken()
        pass

    def move(self, action):
        # self.run.initialize()
        opponent_atsyrau = self.opponent.atsyrau()
        done = False
        info = {}

        home = self.run.home
        home_gamer = self.run

        opponent_side = False
        otau = action
        kumalaks = home[action].move()
        tuzduk_kazan: Kazan = self.opponent_gamer(home_gamer).kazan

        if kumalaks > 1:
            home[otau].add(tuzduk_kazan)
        elif kumalaks == 1:
            kumalaks += 1
        else:
            raise Exception("Игрок не может ходить с лунки где не имеется кумалаков")

        for i in range(kumalaks - 1):
            otau += 1

            if otau % 9 == 0:
                opponent_side = not opponent_side
                home_gamer = self.opponent_gamer(home_gamer)
                tuzduk_kazan: Kazan = self.opponent_gamer(home_gamer).kazan
                home = self.switch_home(home_gamer)
                otau = 0
                pass

            home[otau].add(tuzduk_kazan)
            # if home_gamer.add_home(self.run, otau, tuzduk_kazan):
            #     if opponent_side:
            #         self.run.get_self_tuzduk = True
            #         pass
            #     else:
            #         self.run.get_opponent_tuzduk = True
            #         pass
            #     pass
            # pass

        if opponent_side:
            self.run.last_ball_opponent_home = True
            if home[otau].kumalaks % 2 == 0:
                self.take(home[otau])
                pass
            if home[otau].kumalaks == 3 and otau != 9 and not self.run.tuzduk_announced and home[otau].serial != action:
                home[otau].tuzduk = True
                self.run.tuzduk_announced = True
                self.run.tuzduk_announced_feature = True
                self.take(home[otau])
                pass
            pass
        else:
            self.run.last_ball_opponent_home = False
            pass

        if self.run.kazan.score > 81:
            self.win_gamer(self.run)
            done = True
            pass

        if self.opponent.kazan.score > 81:
            self.win_gamer(self.opponent)
            done = True
            pass

        if self.opponent.atsyrau():
            self.win_gamer(self.run)
            done = True
            pass
        else:
            if opponent_atsyrau:
                self.run.out_opponent_atsyrau = True
                pass
            pass

        if self.run.kazan.score == 81 and self.opponent.kazan.score == 81:
            done = True
            pass

        observation, reward = self.observation(), self.reward
        self.switch_gamer()
        return observation, reward, done, info

    def print(self):

        names = [
            ['Название лунок'],
            ['Номера лунок'],
            ['Черный игрок'],
            ['Белый игрок'],
            ['Номера лунок'],
            ['Название лунок']
        ]

        col_width = [14]

        for i in range(9):
            names[0].append(self.gamers['black'].home[8 - i].name)
            names[1].append("№%s" % (9 - i))
            names[2].append(self.gamers['black'].home[8 - i])

            names[3].append(self.gamers['white'].home[i])
            names[4].append("№%s" % (i + 1))
            names[5].append(self.gamers['white'].home[i].name)

            col_width.append(11)
            pass

        names[0].append("Қазан")
        names[1].append("")
        names[2].append("Қостаушы %s" % self.gamers['black'].kazan.score)

        names[3].append("Бастаушы %s" % self.gamers['white'].kazan.score)
        names[4].append("")
        names[5].append("Қазан")

        col_width.append(12)

        table = texttable.Texttable()
        table.set_cols_width(col_width)
        table.add_rows(names, header=False)
        print(table.draw())

        pass

    pass


if __name__ == '__main__':
    board = Board()
    # # W
    # board.move(0)
    # board.print()
    # # B
    # board.move(1)
    # board.print()
    # # W
    # board.move(1)
    # board.print()
    # # B
    # board.move(8)
    # board.print()
    # # W
    # board.move(0)
    # board.print()
    # # B
    # board.move(8)
    # board.print()
    # # W
    # board.move(6)
    # board.print()
    # # B
    # board.move(6)
    # board.print()
    # # W
    # board.move(2)
    # board.print()
    # # B
    # board.move(8)
    # board.print()
    # # W
    # board.move(2)
    # board.print()
    # # B
    # board.move(4)
    # board.print()
    # # W
    # board.move(4)
    # board.print()
    # # B
    # # board.move(8)
    # # board.print()
    # # board.move(5)
    # # board.print()

    # r = []
    # for i in range(100):
    #     board = Board()
    #
    #     d = False
    #     j = 0
    #     while not d:
    #         j += 1
    #         obs, rew, d, _ = board.move(board.sample_action())
    #         pass
    #     r.append(j)
    #
    # print(np.mean(np.array(r)))
