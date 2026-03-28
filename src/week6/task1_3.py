#task1_3.py 

import matplotlib.pyplot as plt
import os
from keras.preprocessing.image import load_img
from keras.preprocessing.image import save_img
from keras.preprocessing.image import img_to_array

# load image as grayscale
img_path = 'insect.jpg'
img = load_img(img_path, color_mode='grayscale')

# convert to array
img_array = img_to_array(img)

# save image
save_path = 'insect_grayscale.jpg'
save_img(save_path, img_array)

# reload image
img = load_img(save_path)

print(type(img))
print(img.format)
print(img.mode)
print(img.size)

# display image
plt.imshow(img)
plt.axis('off')
plt.show()