import numpy as np
import matplotlib.pyplot as plt

# Task 1: Generate Bernoulli random variables
p = 0.7
X = np.random.binomial(1, p, size=(500, 100))
print("Random variables:", X)

# Task 2: Calculate the sum
S = np.sum(X, axis=0)
print("Sum:", S)

# Task 3: Draw the histogram
plt.hist(S, bins=15, edgecolor="black")
plt.title("Histogram of Bernoulli Sums")
plt.xlabel("Sum")
plt.ylabel("Frequency")
plt.show()

# Task 4: Calculate the deviation
average = S / 500
deviation = average - p

print("Deviation:", deviation)
print("Absolute deviation:", np.abs(deviation))