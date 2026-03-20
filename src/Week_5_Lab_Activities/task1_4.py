# task1_4.py

import numpy as np

# Create 3D array of ones
arr = np.ones((2, 2, 3), dtype=int)

# Assign value 5 at position [1, 0, 2]
arr[1, 0, 2] = 5

# Print array
print(arr)
