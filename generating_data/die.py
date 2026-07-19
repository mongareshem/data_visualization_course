import pygal

from random import randint

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and the number of sides"""
        return randint(1, self.num_sides)

die = Die()

# Make some rolls and store the results in a list
results = [die.roll() for roll_num in range(1000)]
print(results)

# Analyze the results
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]
print(frequencies)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(x) for x in range(1,7)]
hist.x_title ='Result'
hist.y_title = 'Frequency of the Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
