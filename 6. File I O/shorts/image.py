# Pillow library: to do things to images.

from PIL import Image
# we have imported the image object from pillow library.

# to access image filters in pil library :
from PIL import ImageFilter

def main():
    with Image.open("in.jpeg") as img:
        # print(img.size)
        # print(img.format)

        # To rotate the image:
        img = img.rotate(180)

        # To apply blur filter to img:
        img = img.filter(ImageFilter.BLUR)

        # To find edges of the image.
        img = img.filter(ImageFilter.FIND_EDGES)

        img.save("out.jpeg")



main()