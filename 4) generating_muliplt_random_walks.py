import matplotlib.pyplot as plt
from random_walk_class import RandomWalk

# Keep making new walks, as long as the porgram is active
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()

    # ---------- 4) Adding plot points. ----------
    # rw = RandomWalk(50000)

    rw.fill_walk()

    # ---------- 5) Altering the size to fill the screen. ----------
    # Set the size of the plotting window
    plt.figure(figsize=(10, 6))

    plt.scatter(rw.x_values, rw.y_values, s=15)
    # plt.show()

    # ---------- 1) Styling the walk. ----------
    # Coloring the Points
    # Generate a list of numbers equal to the number of points in the walk.
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                cmap=plt.cm.Blues, edgecolors='none', s=15)
    # plt.show()

    # ---------- 2) Plotting the sttartin and ending points. ----------
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1],
                c='red', edgecolors='none', s=100)
    plt.show()

    # ---------- 3) Cleaning up the axes. ----------
    # Remove the axes.
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    # plt.show()

    keep_running = input("Make another walk> (y/n): ")
    if keep_running == 'n':
        break
