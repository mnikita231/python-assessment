from PIL import Image, ImageFilter

image = Image.open('shrimp1.png')

blur = image.filter(ImageFilter.BLUR)
edge = image.filter(ImageFilter.FIND_EDGES)

blur.show()
edge.show()
