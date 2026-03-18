from PIL import Image, ImageEnhance

image = Image.open('shrimp1.png')

sharp = ImageEnhance.Sharpness(image).enhance(2.0)
bright = ImageEnhance.Brightness(image).enhance(1.5)

sharp.show()
bright.show()
