#task1_2.py 

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import array_to_img

# load image (make sure insect.jpg is in the same folder)
img_path = 'insect.jpg'
img = load_img(img_path)

print(type(img))

# convert to numpy array
img_array = img_to_array(img)

print(img_array.dtype)
print(img_array.shape)

# convert back to image
img_pil = array_to_img(img_array)

print(type(img_pil))