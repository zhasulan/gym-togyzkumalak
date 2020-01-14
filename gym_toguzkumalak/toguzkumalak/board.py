import texttable

from gym_toguzkumalak.toguzkumalak.gamer import Gamer
from gym_toguzkumalak.toguzkumalak.kazan import Kazan

import numpy as np


class Board:

    def __init__(self):

        self.gamers = {
            'white': Gamer('white'),
            'black': Gamer('black')
        }

        self.run: Gamer = self.gamers['white']
        self.opponent: Gamer = self.gamers['black']

        pass

    def opponent_gamer(self, gamer: Gamer) -> Gamer:
        return self.gamers['white'] if gamer.name == 'black' else self.gamers['black']

    def switch_gamer(self, gamer: Gamer):
        self.run = self.gamers['white'] if gamer.name == 'black' else self.gamers['black']
        self.opponent = gamer
        pass

    def switch_home(self):
        return self.gamers['white'].home if self.run.name == 'black' else self.gamers['black'].home

    def win_gamer(self, gamer: Gamer):
        gamer.reward = 1
        self.opponent_gamer(gamer).reward = -1
        pass

    def sample_action(self):
        try:
            return self.run.sample_action()
        except IndexError:
            self.win_gamer(self.opponent)
            raise Exception("Более отстутствуют ходы")
        pass

    def observation(self):
        return np.array(self.run.observation() + self.opponent.observation())

    def reward(self):
        return np.array([self.run.reward, self.opponent.reward])

    def move(self, action):
        done = False
        info = {}

        home = self.run.home
        home_gamer = self.run

        take_if_opponent = False
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
                take_if_opponent = not take_if_opponent
                home_gamer = self.opponent_gamer(home_gamer)
                tuzduk_kazan: Kazan = self.opponent_gamer(home_gamer).kazan
                home = self.switch_home()
                otau = 0
                pass

            home[otau].add(tuzduk_kazan)
            pass

        if take_if_opponent:
            if home[otau].kumalaks % 2 == 0:
                self.run.add(home[otau].kumalaks)
                home[otau].taken()
                pass
            if home[otau].kumalaks == 3 and otau != 9 and not self.run.tuzduk_announced:
                home[otau].tuzduk = True
                self.run.tuzduk_announced = True
                self.run.add(home[otau].kumalaks)
                home[otau].taken()
                pass
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

        if not done:
            self.switch_gamer(self.run)

        return self.observation(), self.reward(), done, info

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
            names[1].append("№%s" % (8 - i))
            names[2].append(self.gamers['black'].home[8 - i])

            names[3].append(self.gamers['white'].home[i])
            names[4].append("№%s" % i)
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
    board.move(0)
    board.print()
    board.move(1)
    board.print()
    # board.move(0)
    # board.print()
