import cv2
img1 = cv2.imread('image.png')
img2 = cv2.imread('image2.png')
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
blend = cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow('Blend', blend)
cv2.waitKey(0); cv2.destroyAllWindows()
