import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk and plot the points
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Set the size of the plotting window
    plt.figure(dpi=100, figsize=(10, 6)) #type: ignore

    # Plot the points and show the plot
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, color='purple', linewidth=1.5)

    # Remove the axes
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    # plt.axis('off') # An alternative

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break