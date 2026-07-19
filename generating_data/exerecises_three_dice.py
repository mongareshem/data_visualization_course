import pygal
from random import randint

class Die:
    """Simulation of rolling a D6"""
    def __init__(self, sides=6):
        """Initialize attributes"""
        self.sides = sides

    def roll(self):
        """Simulate a roll"""
        return randint(1, self.sides)


die_1 = Die()
die_2 = Die()
die_3 = Die()

results = [die_1.roll() + die_2.roll() + die_3.roll() for i in range(1000000)]
print(results)

max_result = die_1.sides + die_2.sides + die_3.sides
frequencies = [results.count(value) for value in range(3, max_result + 1)]
print(frequencies)