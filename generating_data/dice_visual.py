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

die_1 = Die()
die_2 = Die()

# Make some rolls and store the results in a list
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]
print(results)

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]
print(frequencies)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [str(i) for i in range(2, 12)]
hist.x_title ='Result'
hist.y_title = 'Frequency of the Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
