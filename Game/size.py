from PIL import Image, ImageEnhance, ImageFilter
import os


img1 = Image.open("images/galaxy.jpg")
#!image size
MAX_SIZE = (1400,800)
img1.thumbnail(MAX_SIZE)
img1.save('images/galaxy.jpg')

# img = Image.new('RGBA', (100, 100), (255, 0, 0, 0))
# img.save("images/alienShip.png", "GIF", transparency=1)
