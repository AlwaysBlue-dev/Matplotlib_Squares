# Plotting the random walk.

import matplotlib.pyplot as plt
from random_walk_class import RandomWalk

# Make a radnom walk, and plot the points
rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
