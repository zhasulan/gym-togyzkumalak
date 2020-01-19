class Kazan:

    def __init__(self):
        self.score = 0
        pass

    def add(self, kumalaks):
        self.score += kumalaks
        pass

    def __str__(self):
        return self.score

    def observation(self):
        return min(self.score, 82) / 82

    pass
