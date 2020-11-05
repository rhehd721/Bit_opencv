from PIL import Image

path = "/home/ubuntu/pythonProject/data/lena.jpg"

im = Image.open(path)
size = (64, 64)
im.thumbnail(size)

print(im.size)
im.show()


outpath = "/home/ubuntu/pythonProject/data/thumbnail_lena.jpg"
im.save(outpath)