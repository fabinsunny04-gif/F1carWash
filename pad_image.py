import sys
from PIL import Image

def make_square(im, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

try:
    img = Image.open('images/logo.png')
    img = img.convert('RGBA')
    square_img = make_square(img)
    square_img.save('images/favicon.png', 'PNG')
    print("Successfully padded image.")
except Exception as e:
    print(f"Error: {e}")
