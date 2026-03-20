# task1_9.py

import numpy as np

temps = np.array([
    [[10, 15, 20], [25, 30, 35]],
    [[11, 16, 21], [26, 31, 36]]
])

# Get second location (index 1), all years and months
result = temps[:, 1, :]

print(result)