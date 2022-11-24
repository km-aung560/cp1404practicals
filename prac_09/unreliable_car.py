from prac_09.car import Car
from random import randint

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(self, name)
        self.fuel = fuel
        self.reliability = reliability

    def drive(self, distance):
        drive_chance = randint(0, 100)
        if drive_chance >= self.reliability:
            print("Your car has broken down")
        distance_driven = super().drive(distance)
        return distance_driven








