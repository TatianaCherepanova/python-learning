from PIL import Image, ImageDraw, ImageColor
import math

img = Image.new("RGBA", (1024, 768))
draw = ImageDraw.Draw(img)


class AnimalColors:
    def __init__(self, line="black", body="grey", eye="yellow", nose="white"):
        self.line = line
        self.body = body
        self.eye = eye
        self.nose = nose
        dark_color = ImageColor.getrgb(body)
        r, g, b = dark_color
        self.dark_zone = (int(r * 0.9), int(g * 0.9), int(b * 0.9))


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
    draw_circle(c, finger_r, colors.dark_zone, colors.line)


def draw_animal_body(xy, r, colors):
    draw_circle(xy, r, colors.body, colors.line)
    angles = [7/6, 5/4, 4/3, 5/3, 7/4, 11/6]
    for angle in angles:
        draw_finger(xy, r, math.pi * angle, r / 10, colors)


def draw_animal_eye(xy, r, colors, is_eyelid=True):
    draw_circle(xy, r, colors.eye, colors.line)
    draw_circle(xy, r / 3, colors.line, colors.line)
    if is_eyelid:
        draw_animal_eyelid(xy, r, colors.dark_zone, colors.line)


def draw_animal_eyelid(xy, r, color, outline):
    """Starting angle, in degrees. Angles are measured from 3 o’clock,
    increasing clockwise.
    Ending angle, in degrees."""
    x, y = xy
    start = 180
    end = 0
    draw.chord([(x - r, y - r), (x + r, y + r)], start, end, color, outline)


def angle_step(xy, height, angle):
    x, y = xy
    x1 = x + height * math.cos(angle)
    y1 = y - height * math.sin(angle)
    return x1, y1


def draw_cat_ear(xy, r, angle, colors):
    height = r + 0.8 * r
    c = angle_step(xy, height, angle)
    b = angle_step(xy, r, angle - 0.5)
    a = angle_step(xy, r, angle + 0.5)
    draw.polygon([c, b, a], colors.dark_zone, colors.line)


def draw_cat_whiskers(xy, r, color):
    """функция рисования усов
    принимает список из двух координат в виде тьюпла
    to - расчет второй точки на окружности головы
    height - длина усов"""
    angles = [195, 210, 225, 315, 330, 345]
    height = r * 1.5
    for angle in angles:
        to = angle_step(xy, height, math.radians(angle))
        draw.line([xy, to], fill=color)


def draw_cat_mouth(xy, r, color):
    angles = [240, 300]
    height = r * 0.3
    for angle in angles:
        to = angle_step(xy, height, math.radians(angle))
        draw.line([xy, to], fill=color)


def draw_cat_face(xy, r, colors): 
    """ xy - координаты центральной точки головы
        r - радиус головы"""            
    x, y = xy
    width = r / 3
    y_shift = r / 5
    y_shift_d = r / 5
    a = (x - width / 2, y + y_shift)
    b = (x + width / 2, y + y_shift)
    c = angle_step(b, width, math.radians(180 + 60))
    d = (x, y + y_shift_d)
    draw_cat_whiskers(d, r, colors.line)
    draw_cat_mouth(c, r, colors.line)
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
    draw_cat_face(xy, r, colors)


def draw_cat_tail(xy, r, angle, colors):
    # y_shift = r / 6
    width = r / 9
    height = 1.5 * r
    a = angle_step(xy, r, angle - width / r)
    b = angle_step(xy, r, angle + width / r) 
    # a = angle_step(xy, width / 2, angle - math.radians(90))
    # b = angle_step(xy, width / 2, angle + math.radians(90))
    c = angle_step(b, height, angle)
    d = angle_step(a, height, angle)
    draw.polygon([a, b, c, d], colors.dark_zone, colors.line)


def draw_cat(xy, r, colors=AnimalColors()):
    draw_animal_body(xy, r, colors)
    x, y = xy
    draw_cat_head((x, y - r / 3), r / 1.2, colors)
    draw_cat_tail(xy, r, math.radians(30), colors)


def draw_dog_mouth(xy, r, color):
    x, y = xy
    width = r / 3 * 2
    height = width / 3 * 2
    wiskers = []
    draw.arc(
      [
        (x - width, y),
        (x, y + height)
      ],
      0, 200, color
    )
    wiskers.append((x - width / 3, y + height / 3))
    wiskers.append((x - width / 2, y + 2 * height / 3))
    wiskers.append((x - 2 * width / 3, y + height / 3))
    draw.arc(
      [
        (x, y),
        (x + width, y + height)
      ],
      340, 180, color
    )
    draw.point(wiskers, color)


def draw_dog_face(xy, r, colors):
    x, y = xy
    width = r / 3
    height = width * 3 / 4
    # TODO: under construction
    draw_dog_mouth(xy, r, colors.line)
    # рисуем нос
    draw.rectangle(
        [
            (x - width / 3 / 2, y),
            (x + width / 3 / 2, y + height)
        ],
        colors.nose,
        colors.line
    )
    draw.rectangle(
        [
            (x - width / 2, y),
            (x + width / 2, y + 2 * height / 3)
        ],
        colors.nose,
        colors.line
    )


def draw_dog_ear(xy, r, colors):
    x, y = xy
    width = r
    height = width
    draw.ellipse([(x - width / 4, y - height / 1.5), (x + width / 4, y + height / 1.5)], colors.dark_zone, colors.line)


def draw_dog_head(xy, r, colors):
    x, y = xy
    x_shift = r / 2.5
    y_shift = r / 5
    eye_r = r / 3
    ear_r = r / 2
    x_shift_ear = r
    y_shift_ear = r / 7
    # draw_cat_ear(xy, r, math.radians(45), colors)
    # draw_cat_ear(xy, r, math.radians(135), colors)
    draw_circle(xy, r, colors.body, colors.line)
    draw_animal_eye((x - x_shift, y - y_shift), eye_r, colors, False)
    draw_animal_eye((x + x_shift, y - y_shift), eye_r, colors)
    draw_dog_face((x, y + r / 5), r, colors)
    draw_dog_ear((x - x_shift_ear, y + y_shift_ear), r, colors)
    draw_dog_ear((x + x_shift_ear, y + y_shift_ear), r, colors)


def draw_dog_tail(a, r, angle, colors):
    #lengh = r * 1.3
    #width = r / 2
    lengh = r * 2
    width = r / 2
    ab = lengh
    b = angle_step(a, ab, angle)

    angle_abc = math.radians(90)
    bc = width
    c = angle_step(b, bc, angle + angle_abc)
    
    angle_bcd = math.radians(45)
    cd = width / 2 / math.cos(angle_bcd)
    d = angle_step(c, cd, angle - math.radians(90) - angle_bcd)

    angle_cde = math.radians(90)
    catet = width / 2 / 3 * 2
    de = math.sqrt(catet ** 2 + catet ** 2)
    angle_cdz = math.radians(180 - 90) - angle_bcd
    e = angle_step(d, de, angle + angle_cdz + angle_cde)

    angle_def = math.radians(80)
    op = width / 2 / 3
    angle_edo = math.radians(180) - angle_cdz - angle_cde
    oe = math.sin(angle_edo) * de
    ep = op + oe
    angle_dep = math.radians(180 - 90) - angle_edo
    angle_pef = angle_def - angle_dep
    ef = ep / math.cos(angle_pef)
    f = angle_step(e, ef, angle - (math.radians(90) - angle_dep) - angle_def)

    angle_efg = math.radians(30)
    fg = ef / 2
    angle_pfe = math.radians(180 - 90) - angle_pef
    g = angle_step(f, fg, angle + angle_pfe + angle_efg)

    angle_fgh = math.radians(50)
    angle_pfg = angle_pfe + angle_efg
    angle_kgf = math.radians(180 - 90) - angle_pfg
    #TODO angle_pfg can be negative
    assert angle_kgf >= 0 
    angle_kgh = angle_kgf + angle_fgh
    kg = math.sin(angle_pfg) * fg
    gh = kg / math.cos(angle_kgh)
    h = angle_step(g, gh, angle - math.radians(90) - angle_kgh)
    
    draw.polygon([a, b, c, d, e, f, g, h], colors.dark_zone, colors.line)


def draw_dog(xy, r, colors=AnimalColors()):
    draw_dog_tail(xy, r, math.radians(150), colors)
    draw_animal_body(xy, r, colors)
    x, y = xy
    draw_dog_head((x, y - r / 3), r / 1.5, colors)



def main():
    cats = [
        ((250, 300), 80, AnimalColors(line="violet", body="white", eye="blue", nose="black")),
        ((420, 380), 50, AnimalColors(body="red", eye="blue")),
        ((500, 600), 100, AnimalColors(line="white", body="magenta", eye="green", nose="pink")),

        ((150, 600), 90, AnimalColors(body="purple"))
    ]
    for cat in cats:
        draw_cat(*cat)
    for (x, y), sz, colors in cats:
        draw_cat((x, y + 40), sz, colors)

    def archimedean_spiral(xy, k, sigma):
        return angle_step(xy, k * sigma, sigma)

    def adjacent_pairs(it):
        try:
            it = iter(it)
            a, b = next(it), next(it)
            while True:
                yield a, b
                a, b = b, next(it)
        except StopIteration:
            pass

    archimedean_step = 15
    for start, end in adjacent_pairs(
        archimedean_spiral((img.width / 2, img.height / 2), archimedean_step, math.radians(i))
        for i in range(
            0,
            int(math.degrees(max(img.height, img.width) / archimedean_step))
        )
    ):
        draw.line([start, end])

    draw_dog((750, 250), 160, AnimalColors(body="#6D4C41", nose="black", eye="#69F0AE"))
    # c = img.rotate(30)

    # n = Image.merge("RGB", img.split()[0:-1])
    # img.paste(c, mask=c)
    # c.split()[3].show()
    # n.show()

    # for l in n.split():
    #    l.show()
    img.show()

    # math.radians
    # 1 тело котика - done
    # 2 мордочка:
    # 3 хвост


if __name__ == "__main__":
    main()

