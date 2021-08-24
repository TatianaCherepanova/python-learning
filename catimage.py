from PIL import Image, ImageDraw
import math

img = Image.new("RGB", (1024, 768))
draw = ImageDraw.Draw(img)

class cat_colors:
    def __init__(self, line = "black", body = "grey", eye = "yellow", nose = "white"):
        self.line = line
        self.body = body
        self.eye = eye
        self.nose = nose

#v = cat_colors("white", "red")
#h = cat_colors(eye="blue", body="red")
#a = cat_colors("red", "red", "blue", "magenta")


#print(a.body)
#print(a.nose)

#b = cat_colors("blue", "red", "blue", "white")
#print(a.nose)
#print(b.nose)

#c = cat_colors("blue", "red", "blue", "white")

def draw_circle(xy, r, fill=None, outline=None):    
    """ функция для рисования тела животного
        xy - координаты центра
        r - радиус"""
    x, y = xy
    draw.ellipse([(x - r, y - r), (x + r, y + r)], fill, outline)

def draw_finger(xy, r, angle, finger_r, colors):
    """функция для рисования меньшего круга с 
       центром на окружности большого круга"""
    c = angle_step(xy, r, angle)
    draw_circle(c, finger_r, colors.body, colors.line)

def draw_animal_body(xy, r, colors):
    draw_circle(xy, r, colors.body, colors.line)
    angles = [7/6, 5/4, 4/3, 5/3, 7/4, 11/6]
    for angle in angles:
        draw_finger(xy, r, math.pi * angle, r / 10, colors)

def draw_animal_eye(xy, r, colors):
    draw_circle(xy, r, colors.eye, colors.line)
    draw_circle(xy, r / 3, colors.line, colors.line)

def angle_step(xy, height, angle):
    x, y = xy
    x1 = x + height * math.cos(angle)
    y1 = y - height * math.sin(angle)
    return (x1, y1)

def draw_cat_ear(xy, r, angle, colors):
    height = r + 0.8 * r
    c = angle_step(xy, height, angle)
    b = angle_step(xy, r, angle - 0.5)
    a = angle_step(xy, r, angle + 0.5)
    draw.polygon([c, b, a], colors.body, colors.line)

def draw_cat_nose(xy, r, colors): 
    """ xy - координаты центральной точки головы
        r - радиус головы"""            
    x, y = xy
    width = r / 3
    y_shift = r / 5  
    a = (x - width / 2, y + y_shift)
    b = (x + width / 2, y + y_shift)
    c = angle_step(b, width, math.radians(180 + 60))
    draw.polygon([c, b, a], colors.nose, colors.line)

def draw_cat_head(xy, r, colors):
    x, y = xy
    x_shift = r / 2.5 
    y_shift = r / 5
    eye_r = r / 3
    draw_cat_ear(xy, r, math.radians(45), colors)
    draw_cat_ear(xy, r, math.radians(135), colors)
    draw_circle(xy, r, colors.body, colors.line)
    draw_animal_eye((x - x_shift, y - y_shift), eye_r, colors)
    draw_animal_eye((x + x_shift, y - y_shift), eye_r, colors)
    draw_cat_nose(xy, r, colors)

def draw_cat_tail(xy, r, angle, colors):
    x, y = xy
    #y_shift = r / 6
    width = r / 9
    hight = 1.5 * r
    a = angle_step(xy, r, angle - width / r)
    b = angle_step(xy, r, angle + width / r) 
    #a = angle_step(xy, width / 2, angle - math.radians(90))
    #b = angle_step(xy, width / 2, angle + math.radians(90))
    c = angle_step(b, hight, angle)
    d = angle_step(a, hight, angle)
    draw.polygon([a, b, c, d], colors.body, colors.line)

def draw_cat(xy, r, colors=cat_colors()):
    draw_animal_body(xy, r, colors)
    x, y = xy
    draw_cat_head((x, y - r / 3), r / 1.2, colors)
    draw_cat_tail(xy, r, math.radians(30), colors)

draw_cat((250, 300), 80)
draw_cat((420, 380), 50, cat_colors(body="red", eye="blue"))
draw_cat((500, 600), 100, cat_colors(line="white", body="magenta", eye="green", nose="pink"))
draw_cat((750, 250), 160, cat_colors(line="violet", body="white", eye="blue", nose="black"))

img.show()

#math.radians
#1 тело котика - done
#2 мордочка:
#3 хвост 
