import cv2
img = cv2.imread('image.png')
resized = cv2.resize(img, (400,300))
cv2.imshow('Resized', resized)
cv2.waitKey(0); cv2.destroyAllWindows()
