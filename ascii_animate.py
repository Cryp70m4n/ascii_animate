import time
from PIL import Image
import sys
import os

CLIP_FRAMES = int(sys.argv[1])
print (CLIP_FRAMES)
ASCII_CHARS = ['⠀','⠄','⠆','⠖','⠶','⡶','⣩','⣪','⣫','⣾','⣿']
ASCII_CHARS.reverse()
ASCII_CHARS = ASCII_CHARS[::-1]

WIDTH = 60

def resize(image, new_width=WIDTH):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int((aspect_ratio * new_width)/2.5)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image

def grayscalify(image):
    return image.convert('L')

def modify(image, buckets=25):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

def do(image, new_width=WIDTH):
    image = resize(image)
    image = grayscalify(image)

    pixels = modify(image)
    len_pixels = len(pixels)

    new_image = [pixels[index:index+int(new_width)] for index in range(0, len_pixels, int(new_width))]

    return '\n'.join(new_image)

def opener(path):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        print("Error with path:", path)
        return
    image = do(image)

    return image

frames = []

for i in range(CLIP_FRAMES):
    path = "frames/frame"+str(i)+".jpg"
    frames.append(opener(path))


while True:
    try:
        print(f"{frames[i]}")
        time.sleep(0.2)
        os.system("clear")
        i+=1
        if (i)>=CLIP_FRAMES:
            i=0
    except Exception as e:
        i=0
        print(e)
