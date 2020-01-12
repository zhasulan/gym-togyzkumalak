from toguzkumalak.kazan import Kazan


class Otau:

    def __init__(self, serial, name):
        self.name = name
        self.serial = serial
        self.kumalak_count = 9
        self.tuzduk = False
        pass

    def __str__(self):
        if self.tuzduk:
            return "X"
        if self.kumalak_count == 0:
            return "–"
        return str(self.kumalak_count)

    def move(self):
        kumalak_count = self.kumalak_count
        self.kumalak_count = 0
        return kumalak_count

    def add(self, opponent_kazan: Kazan):
        if self.tuzduk:
            opponent_kazan.add(1)
        else:
            self.kumalak_count += 1
        pass

    def taken(self):
        self.kumalak_count = 0
        pass

    pass
