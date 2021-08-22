from PIL import Image, ImageDraw
import math

img = Image.new("RGB", (1024, 768))
draw = ImageDraw.Draw(img)

def draw_circle(xy, r):    
    """ функция для рисования тела животного
    xy - координаты центра
    r - радиус"""
    x, y = xy
    draw.ellipse([(x - r, y - r), (x + r, y + r)])

def draw_finger(xy, r, angle, finger_r):
    """функция для рисования меньшего круга с 
    центром на окружности большого круга"""
    x, y = xy
    x1 = x + r * math.cos(angle)
    y1 = y - r * math.sin(angle)
    draw_circle((x1, y1), finger_r)

def draw_animal_body(xy, r):
    draw_circle(xy, r)
    angles = [7/6, 5/4, 4/3, 5/3, 7/4, 11/6]
    for angle in angles:
        draw_finger(xy, r, math.pi * angle, r / 10)

def draw_animal_eye(xy, r):
    draw_circle(xy, r)
    draw_circle(xy, r / 3)

def draw_cat_head(xy, r):
    x, y = xy
    x_shift = r / 2.5 
    y_shift = r / 5
    eye_r = r / 3
    draw_circle(xy, r)
    draw_animal_eye((x - x_shift, y - y_shift), eye_r)
    draw_animal_eye((x + x_shift, y - y_shift), eye_r)

def draw_cat(xy, r):
    draw_animal_body(xy, r)
    x, y = xy
    draw_cat_head((x, y - r / 3), r / 1.2)

draw_cat((250, 300), 80)
draw_cat((350, 400), 50)
draw_cat((500, 600), 100)

img.show()

#math.radians
#1 тело котика - done
#2 мордочка:
#3 хвост 
