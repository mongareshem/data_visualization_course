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
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)