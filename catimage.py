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
    c = angle_step(xy, r, angle)
    draw_circle(c, finger_r)

def draw_animal_body(xy, r):
    draw_circle(xy, r)
    angles = [7/6, 5/4, 4/3, 5/3, 7/4, 11/6]
    for angle in angles:
        draw_finger(xy, r, math.pi * angle, r / 10)

def draw_animal_eye(xy, r):
    draw_circle(xy, r)
    draw_circle(xy, r / 3)

def angle_step(xy, height, angle):
    x, y = xy
    x1 = x + height * math.cos(angle)
    y1 = y - height * math.sin(angle)
    return (x1, y1)

def draw_cat_ear(xy, r, angle):
    height = r + 0.8 * r
    c = angle_step(xy, height, angle)
    b = angle_step(xy, r, angle - 0.5)
    a = angle_step(xy, r, angle + 0.5)
    draw.polygon([c, b, a])

def draw_cat_nose(xy, r): 
    """ xy - координаты центральной точки головы
        r - радиус головы"""            
    x, y = xy
    width = r / 3
    y_shift = r / 5  
    a = (x - width / 2, y + y_shift)
    b = (x + width / 2, y + y_shift)
    c = angle_step(b, width, math.radians(180 + 60))
    draw.polygon([c, b, a])

def draw_cat_head(xy, r):
    x, y = xy
    x_shift = r / 2.5 
    y_shift = r / 5
    eye_r = r / 3
    draw_cat_ear(xy, r, math.radians(45))
    draw_cat_ear(xy, r, math.radians(135))
    draw_circle(xy, r)
    draw_animal_eye((x - x_shift, y - y_shift), eye_r)
    draw_animal_eye((x + x_shift, y - y_shift), eye_r)
    draw_cat_nose(xy, r)

def draw_cat(xy, r):
    draw_animal_body(xy, r)
    x, y = xy
    draw_cat_head((x, y - r / 3), r / 1.2)

draw_cat((250, 300), 80)
draw_cat((420, 380), 50)
draw_cat((500, 600), 100)
draw_cat((750, 250), 160)

img.show()

#math.radians
#1 тело котика - done
#2 мордочка:
#3 хвост 
