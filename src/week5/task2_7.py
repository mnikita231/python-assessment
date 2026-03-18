import cv2, numpy as np
img = cv2.imread('image.png')
inv = 255 - img
combo = np.hstack((img, inv))
cv2.imshow('Invert', combo)
cv2.waitKey(0); cv2.destroyAllWindows()
