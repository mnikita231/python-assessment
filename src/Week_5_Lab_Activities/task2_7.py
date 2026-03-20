# task2_7.py

import cv2
import numpy as np

# Load image
image = cv2.imread('image.png')

# Invert colors
inverted = 255 - image

# Combine original + inverted side by side
combined = np.hstack((image, inverted))

# Show result
cv2.imshow('Original and Inverted', combined)

cv2.waitKey(0)
cv2.destroyAllWindows()