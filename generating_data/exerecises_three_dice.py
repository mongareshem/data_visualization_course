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