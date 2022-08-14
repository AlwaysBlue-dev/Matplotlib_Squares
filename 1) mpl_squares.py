import matplotlib.pyplot as plt

# 1) SIMPLE LINE GRAPH
squares = [1, 4, 9, 16, 25]
plt.plot(squares)

# remove comment (#) to show the plot
# plt.show()

# 2) CHANGING THE LABEL TYPE & GRAPH THICKNESS
plt.plot(squares, linewidth=5)

# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

# remove comment (#) to show the plot
# plt.show()

# 3) CORRECTING THE PLOT
# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Giving input values & changing the default behavior which start from 0
input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squares, linewidth=5)

# remove comment (#) to show the plot
# plt.show()
