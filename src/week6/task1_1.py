#task1_1.py 

import matplotlib.pyplot as plt
from keras.preprocessing.image import load_img

# load image (make sure insect.jpg is in the same folder)
img_path = 'insect.jpg'
img = load_img(img_path)

# print image details
print(type(img))
print(img.format)
print(img.mode)
print(img.size)

# display image
plt.imshow(img)
plt.axis('off')
plt.show()