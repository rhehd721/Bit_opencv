from PIL import Image

path = "/home/ubuntu/pythonProject/data/lena.jpg"

im = Image.open(path)
img2 = im.crop((100, 100, 350, 350))
img2.show()