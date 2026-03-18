import cv2
img = cv2.imread('image.png')
print(img[50,50])
img[50,50] = [255,255,255]
cv2.imwrite('modified.png', img)
