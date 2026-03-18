from PIL import Image

image = Image.open('shrimp1.png')

print(image.size)
print(image.filename)
print(image.format)

image.show()

rotated = image.rotate(30)
rotated.show()
rotated.save('rotated.png')
