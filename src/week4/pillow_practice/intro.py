from PIL import Image

# create an image via import
file_name = 'cat.jpg'

image = Image.open(file_name)

# analyze the image 
print(image.size)
print(image.filename)
print(image.format)

# show the original image
image.show()

# rotate image 30 degrees
cat_rotated = image.rotate(30)

# save rotated image
cat_rotated.save('cat_rotated.png', 'png')

# show rotated image
cat_rotated.show()