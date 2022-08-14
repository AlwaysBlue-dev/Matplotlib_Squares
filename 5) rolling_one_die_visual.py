########### Rolling One Die Visual ###########

from rolling_die_class import Die

# Create a D6 (dice with six numbers)
die = Die()

# Make a class rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(results)
print(frequencies)
