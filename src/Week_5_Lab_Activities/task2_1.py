# task2_1.py

import cv2

# Read image (make sure image.png is in same folder)
image = cv2.imread('image.png')

print(f"Type of the image: {type(image)}")
print(f"Shape of the image array: {image.shape}")
