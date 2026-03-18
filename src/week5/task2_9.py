import cv2
img1 = cv2.imread('image.png')
img2 = cv2.imread('image2.png')
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
cv2.imshow('Add', cv2.add(img1,img2))
cv2.imshow('Sub', cv2.subtract(img1,img2))
cv2.waitKey(0); cv2.destroyAllWindows()
