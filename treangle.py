from math import sqrt 

def square(a, b):
    return a * b // 2
    
def hype(b, c):
    return sqrt(b ** 2 + c ** 2) 

g = hype(6, 3)
s = square(3, 2)

print(s)
print(int(g))

print('Площадь квадратного треугольника равна ' + str(s) + '\nА длина гипотенузы равна ' + str(g))