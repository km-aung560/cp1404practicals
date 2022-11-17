CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def calculate_age(self):
        """Calculate age from current year and guitar age"""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determine if Guitar is more than 50 years old"""
        return Guitar.calculate_age(self) >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year

    def __repr__(self):
        return f"[{self.name}, {self.year}, {self.cost}]"

# def run_tests():
#     guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
#     other = Guitar("Another Guitar", 2013, 15000)
#     print(guitar < other)
#
#
# if __name__ == '__main__':
#     run_tests()
