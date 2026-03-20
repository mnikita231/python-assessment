# task2_4.py

import cv2

# Read image
image = cv2.imread('image.png')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('gray_image.png', gray_image)

print("Grayscale image saved as gray_image.png")
