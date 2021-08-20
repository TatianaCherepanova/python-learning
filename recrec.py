from PIL import Image, ImageDraw
import random

img = Image.new("RGB", (1024, 768))
draw = ImageDraw.Draw(img)
#colors = ["red", "white", "pink", "green", "grey", 
#    "black", "brown", "aqua", "yellow", "blue", "magenta", "orange", "purple"]

def recrec(a, b):
    ax, ay = a
    bx, by = b
    width = bx - ax
    if (width <= 8):
        return
    draw.rectangle([a, b],
        (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    height = by - ay
    recrec((ax + width/8, ay + height/8), (bx - width/8, by - height/8))

recrec((0, 0), (1024, 768)) 
img.show()