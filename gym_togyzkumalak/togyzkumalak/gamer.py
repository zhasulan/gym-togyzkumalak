import random

from gym_togyzkumalak.togyzkumalak.kazan import Kazan
from gym_togyzkumalak.togyzkumalak.otau import Otau


class Gamer:

    def __init__(self, name):
        self.tuzduk_announced = False
        self.name = name

        self.home = {
            0: Otau(0, 'Арт'),
            1: Otau(1, 'Тектұрмас'),
            2: Otau(2, 'Ат өтпес'),
            3: Otau(3, 'Атсыратар'),
            4: Otau(4, 'Бел'),
            5: Otau(5, 'Белбасар'),
            6: Otau(6, 'Қандықақпан'),
            7: Otau(7, 'Көкмойын'),
            8: Otau(8, 'Маңдай')
        }

        self.kazan = Kazan()

        # # Additional Features
        # # 1 - ход взял шарики в казан; 0 - не брал
        # self.last_taken = False
        # # 1 - в моем ходе мой туздук взял шарик; 0 - не брал
        # self.get_self_tuzduk = False
        # # 1 - в моем ходе туздук оппонента взял шарик; 0 - не брал
        # self.get_opponent_tuzduk = False
        # # 1 - последний шар попал в лунку соперника; 0 - последний шар попал в мою лунку
        # self.last_ball_opponent_home = False
        # # 1 - Ход позвонил создать туздук; 0 - Ход не создал туздук
        # self.tuzduk_announced_feature = False
        # # 1 - Ход позвонил оппоненту выйти из состояния атсырау; 0 - Ход не создал туздук
        # self.out_opponent_atsyrau = False
        pass

    # def initialize(self):
    #     self.last_taken = False
    #     self.get_self_tuzduk = False
    #     self.get_opponent_tuzduk = False
    #     self.last_ball_opponent_home = False
    #     self.tuzduk_announced_feature = False
    #     self.out_opponent_atsyrau = False
    #     pass

    def atsyrau(self):
        for key, otau in self.home.items():
            if otau.kumalaks != 0:
                return False
        return True

    def observation(self, opponent_kazan: Kazan):
        state = []

        for key, otau in self.home.items():
            state += otau.observation()
            pass

        state.append(self.kazan.observation())
        state.append(int(self.kazan.score > opponent_kazan.score))

        # tuzduk = []
        # for key, otau in self.home.items():
        #     state.append(otau.kumalaks)
        #     if otau.tuzduk:
        #         tuzduk.append(1)
        #     else:
        #         tuzduk.append(0)
        #     pass
        # state.append(self.kazan.score)
        # state = state + tuzduk
        #
        # # Если в казане больше соперника
        # if self.kazan.score > opponent_kazan.score:
        #     state.append(1)
        #     pass
        # else:
        #     state.append(0)
        #     pass

        return state

    def sample_action(self):
        a = []
        for key, otau in self.home.items():
            if otau.kumalaks != 0 and not otau.tuzduk:
                a.append(key)
                pass
            pass

        return random.choice(a)

    def check_action(self, action):
        return True if self.home[action].kumalaks > 0 else False

    def add(self, kumalaks):
        self.kazan.add(kumalaks)

        # Features update
        # self.last_taken = True
        pass

    # def add_home(self, run_gamer, otau, tuzduk_kazan):
    #     return self.home[otau].add(tuzduk_kazan)

    def __str__(self):
        return self.name

    pass

    def available_action(self):
        a = []
        for key, otau in self.home.items():
            if otau.kumalaks != 0 and not otau.tuzduk:
                a.append(1)
                pass
            else:
                a.append(0)
                pass
            pass

        return a
