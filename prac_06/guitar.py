class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.year}"

    def get_age(self):
        age = 2022 - self.year
        return age

    def is_vintage(self):
        return Guitar.get_age(self) >= 50
