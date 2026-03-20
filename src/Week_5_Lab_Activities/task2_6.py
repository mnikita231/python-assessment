# task2_6.py


import cv2

# Load image
image = cv2.imread('image.png')

# Print original pixel value at (50, 50)
print(f"Original pixel value at (50, 50): {image[50, 50]}")

# Change pixel to white (BGR → [255, 255, 255])
image[50, 50] = [255, 255, 255]

# Save modified image
cv2.imwrite('modified.png', image)

print("Modified image saved as modified.png")