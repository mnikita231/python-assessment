from PIL import Image

image = Image.open('shrimp1.png')

image_rotate = image.rotate(45)
image_crop = image.crop((0,0,300,300))
image_resize = image.resize((200,200))

image_rotate.show()
image_crop.show()
image_resize.show()
