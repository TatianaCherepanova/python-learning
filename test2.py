from math import sqrt 

def square(a, b):
    return a * b // 2
    
def hype(b, c):
    return sqrt(b ** 2 + c ** 2) 

a = 3
b = 2
g = hype(a, b)
s = square(a, b)

print(s)
print(int(g))

print('''Площадь квадратного треугольника с катетами длинной {a} и {b} равна {s}
А длина гипотенузы треугольника с катетами {a} и {b}, соответственно - {g}
'''
    .format(a=a, b=b, s=s, g=g))