import matplotlib.pyplot as plt
import numpy as np

# Creating a graf of a certain size
plt.figure(figsize=(8,8))

# Create grid
plt.grid(linewidth=0.5)

# Plot Horizontal and vertical lines
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Generate x values
x = np.linspace(-10, 10, 200)

# Compute the corresponding y values
y = x**2

# Plot the parabola
plt.plot(x, y)
