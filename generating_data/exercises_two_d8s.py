import pygal
from random import randint

class Die:
    """A class modeling two D8s"""
    def __init__(self, sides=8):
        """Initialize attributes"""
        self.sides = sides

    def roll(self):
        """Simulation of a roll"""
        return randint(1, self.sides)


die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for i in range(1000000)]
print(results)

max_result = die_1.sides + die_2.sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]
print(frequencies)

hist = pygal.Bar()

hist.title = 'Results of rolling two D8 dice'
hist.x_labels = [str(i) for i in range(2, max_result + 1)]
hist.x_title = 'Results'
hist.y_title = 'Frequency of the results'

hist.add('D8 + D8', frequencies)
hist.render_to_file('exercise_dice.svg')