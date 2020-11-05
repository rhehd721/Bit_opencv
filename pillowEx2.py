from PIL import Image

path = "/home/ubuntu/pythonProject/data/lena.jpg"

im = Image.open(path)
img2 = im.resize((800, 800))
img2.show()