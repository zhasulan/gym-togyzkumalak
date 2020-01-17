from gym_toguzkumalak.toguzkumalak.kazan import Kazan


class Otau:

    def __init__(self, serial, name):
        self.name = name
        self.serial = serial
        self.kumalaks = 9
        self.tuzduk = False
        pass

    def __str__(self):
        if self.tuzduk:
            return "X"
        if self.kumalaks == 0:
            return "–"
        return str(self.kumalaks)

    def move(self):
        kumalaks = self.kumalaks
        self.kumalaks = 0
        return kumalaks

    def add(self, opponent_kazan: Kazan):
        if self.tuzduk:
            opponent_kazan.add(1)
            return True
        else:
            self.kumalaks += 1
            return False
        pass

    def taken(self):
        self.kumalaks = 0
        pass

    pass
