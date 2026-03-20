# task2_5.py

import cv2

# Load image
image = cv2.imread('image.png')

# Make a copy
image_copy = image.copy()

# Draw red circle (BGR → Red = (0, 0, 255))
cv2.circle(image_copy, (100, 100), 50, (0, 0, 255), 3)

# Show image
cv2.imshow('Image with Circle', image_copy)

# Wait + close
cv2.waitKey(0)
cv2.destroyAllWindows()