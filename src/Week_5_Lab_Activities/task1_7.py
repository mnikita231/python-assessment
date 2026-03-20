# task1_7.py

import numpy as np

# Create matrix 1 to 9 reshaped to 3x3
matrix = np.arange(1, 10).reshape(3, 3)

# Create vector
vector = np.array([1, 0, -1])

# Multiply using broadcasting
result = matrix * vector

# Print result
print(result)
