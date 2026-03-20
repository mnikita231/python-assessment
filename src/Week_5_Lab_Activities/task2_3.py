# task2_3.py

import cv2

# Read image
image = cv2.imread('image.png')

# Resize to 400x300 (width, height)
resized_img = cv2.resize(image, (400, 300))

# Display resized image
cv2.imshow('Resized Image', resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
