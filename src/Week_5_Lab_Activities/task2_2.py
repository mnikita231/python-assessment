# task2_2.py

import cv2

# Read image
image = cv2.imread('image.png')

# Split into BGR channels
b, g, r = cv2.split(image)

# Display each channel
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)

cv2.waitKey(0)
cv2.destroyAllWindows()
