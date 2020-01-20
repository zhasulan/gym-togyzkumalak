from gym_togyzkumalak.togyzkumalak.kazan import Kazan


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

    def observation(self):
        if self.serial != 8:
            return [
                int(self.kumalaks >= 1),
                int(self.kumalaks >= 2),
                self.kumalaks % 2,
                (self.kumalaks % 9) / 8,
                (self.kumalaks % 18) / 17,
                self.kumalaks / 9,
                int(self.tuzduk)
            ]
        else:
            return [
                int(self.kumalaks >= 1),
                self.kumalaks % 2,
                (self.kumalaks % 9) / 8,
                (self.kumalaks % 18) / 17,
                self.kumalaks / 9
            ]
        pass

    pass
