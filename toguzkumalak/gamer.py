import random

from toguzkumalak.kazan import Kazan
from toguzkumalak.otau import Otau


class Gamer:

    def __init__(self, name):
        self.tuzduk_announced = False
        self.name = name

        self.home = {
            1: Otau(1, 'Арт'),
            2: Otau(2, 'Тектұрмас'),
            3: Otau(3, 'Ат өтпес'),
            4: Otau(4, 'Атсыратар'),
            5: Otau(5, 'Бел'),
            6: Otau(6, 'Белбасар'),
            7: Otau(7, 'Қандықақпан'),
            8: Otau(8, 'Көкмойын'),
            9: Otau(9, 'Маңдай')
        }

        self.kazan = Kazan()
        self.reward = 0
        pass

    def atsyrau(self):
        for key, otau in self.home.items():
            if otau.kumalak_count != 0:
                return False
        return True

    def sample_action(self):
        a = []
        for key, otau in self.home.items():
            if otau.kumalak_count != 0 and not otau.tuzduk:
                a.append(key)
                pass
            pass

        return random.choice(a)

    def __str__(self):
        return self.name

    def add(self, kumalaks):
        self.kazan.add(kumalaks)
        pass

    pass
