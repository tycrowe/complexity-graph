import math
import matplotlib.pyplot as plt


def O_1(n):
    return 1


def O_log_n(n):
    return math.log(n, 2)


def O_sqrt_n(n):
    return math.sqrt(n)


def O_n(n):
    return n


def O_n_log_n(n):
    return n * math.log(n, 2)


def O_n_squared(n):
    return n ** 2


def O_2_n(n):
    return 2 ** n


def O_n_n(n):
    return math.factorial(n)


input_sizes = range(1, 11)
complexities = [O_1, O_log_n, O_sqrt_n, O_n, O_n_log_n, O_n_squared, O_2_n, O_n_n]

# Initialize the plot
plt.figure(figsize=(12, 8))

# Plot each complexity class
for complexity in complexities:
    operations = [complexity(n) for n in input_sizes]
    plt.plot(input_sizes, operations, label=complexity.__name__)

# Set the y-axis to a logarithmic scale
plt.yscale('log')

# Add labels and a legend
plt.xlabel("Data Input")
plt.ylabel("Operations")
plt.title("Big O' Notation Time Complexity")

# Adjust the x-axis and y-axis limits
plt.xlim(1, max(input_sizes))
plt.ylim(1, max([O_n_n(n) for n in input_sizes]))

# Enable the grid and legend
plt.grid(True, which="both", ls="--")
plt.legend()

# Show the plot
plt.show()
