# task2_10.py


import cv2

# Load image
image = cv2.imread('image.png')

# Convert BGR to HSV
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Split channels
h, s, v = cv2.split(hsv_img)

# Display each channel
cv2.imshow('Hue Channel', h)
cv2.imshow('Saturation Channel', s)
cv2.imshow('Value Channel', v)

cv2.waitKey(0)
cv2.destroyAllWindows()