from PIL import Image, ImageOps

image = Image.open('shrimp1.png')

mirror = ImageOps.mirror(image)
invert = ImageOps.invert(image.convert('RGB'))

mirror.show()
invert.show()

