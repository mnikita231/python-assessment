import cv2
img = cv2.imread('image.png')
b,g,r = cv2.split(img)
cv2.imshow('B', b); cv2.imshow('G', g); cv2.imshow('R', r)
cv2.waitKey(0); cv2.destroyAllWindows()
