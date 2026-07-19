import pygal
from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=25):
        """Initialize attributes of walk"""
        self.num_points  = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Calculate the steps and directions"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        return direction * distance

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

rw = RandomWalk()
rw.fill_walk()
print(max(rw.x_values))
print(min(rw.x_values))
frequencies = [rw.x_values.count(value) for value in range(min(rw.x_values), max(rw.x_values)+1)]
print(frequencies)

hist = pygal.Bar()

hist.title = 'Visualization of the random walk using a histogram'
hist.x_labels = [str(i) for i in range(min(rw.x_values), max(rw.x_values)+1)]
hist.x_title = 'Step Value'
hist.y_title = 'Frequency of the Step Value'

hist.add('RW', frequencies)
hist.render_to_file('exercises_matplotlib_rw.svg')