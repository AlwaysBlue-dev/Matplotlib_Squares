import matplotlib.pyplot as plt

############ NOTE: REMOVE COMMENT(#) FROM THE CODE YOU WANT TO RUN ############

# ------------- 1) Plotting and styling individual points with scatter()-------------
# plt.scatter(2, 4)
# plt.show()

# Style the output
# s -> set the size of dot
# plt.scatter(2, 4, s=200)

# Set chart title and label axes
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
# plt.tick_params(axis='both', which='major', labelsize=14)

# remove comment to show the plot
# plt.show()

# -------------2) Plotting a series of points with scatter()-------------
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.scatter(x_values, y_values, s=100)

# Set chart title and label axes
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
# plt.tick_params(axis='both', which='major', labelsize=14)

# remove comment to show the plot
# plt.show()

# -------------3) Calculating data automatically-------------
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, s=40)

# Set chart title and label axes
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
# plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
# plt.axis([0, 1100, 0, 1100000])

# Removing the values in exponent 'le6'
# plt.ticklabel_format(style='plain')

# remove comment to show the plot
# plt.show()

# ------------- 4) Removing outlines from data Points-------------
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]

# add one more argument 'edgecolor'
# plt.scatter(x_values, y_values, edgecolor='none', s=40)

# Set chart title and label axes
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
# plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
# plt.axis([0, 1100, 0, 1100000])

# remove comment to show the plot
# plt.show()

# -------------5) Defining custom colors-------------
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]

# changing the color
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)

# using RGB to change the color
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

# Set chart title and label axes
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
# plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
# plt.axis([0, 1100, 0, 1100000])

# remove comment to show the plot
# plt.show()

# -------------6) Using colormap-------------
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]

# This code colors the points with lower y-values light blue and the points with larger y-values dark blue
# plt.scatter(x_values, y_values, c=y_values,
#             cmap=plt.cm.Blues, edgecolors='none', s=40)

# Set chart title and label axes
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
# plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
# plt.axis([0, 1100, 0, 1100000])

# remove comment to show the plot
# plt.show()

# -------------7) Saving you plot automatically-------------
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, s=40)

# Set chart title and label axes
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
# plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
# plt.axis([0, 1100, 0, 1100000])

# remove comment to show the plot
# plt.show()

# remove comment to save the plot
# plt.savefig("squares_plot.png", bbox_inces="tight")