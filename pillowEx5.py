from PIL import Image, ImageFilter

path = "/home/ubuntu/pythonProject/data/lena.jpg"

im = Image.open(path)
img2 = im.filter((ImageFilter.BLUR))
img2.show()