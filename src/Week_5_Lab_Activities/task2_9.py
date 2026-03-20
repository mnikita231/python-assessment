# task2_9.py

import cv2

# Load image
img1 = cv2.imread('image.png')

# Create grayscale version (same as Task 2_8)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# Resize (just to follow instructions)
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Perform operations
added = cv2.add(img1, img2_resized)
subtracted = cv2.subtract(img1, img2_resized)

# Show results
cv2.imshow('Added Image', added)
cv2.imshow('Subtracted Image', subtracted)

cv2.waitKey(0)
cv2.destroyAllWindows()