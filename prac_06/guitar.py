class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.year}"

    def calculate_age(self):
        """Calculate age from current year and guitar age"""
        age = 2022 - self.year
        return age

    def is_vintage(self):
        """Determine if Guitar is more than 50 years old"""
        return Guitar.calculate_age(self) >= 50
