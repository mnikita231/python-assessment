import cv2
img = cv2.imread('image.png')
copy = img.copy()
cv2.circle(copy, (100,100), 50, (0,0,255), 3)
cv2.imshow('Circle', copy)
cv2.waitKey(0); cv2.destroyAllWindows()
