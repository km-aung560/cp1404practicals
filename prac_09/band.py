from prac_09.musician import Musician

class Band(Musician):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.musicians = []

    def __str__(self):
        return f"{self.name} {self.musicians} "

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        pass
