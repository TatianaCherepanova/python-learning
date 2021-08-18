True       // bool
False      // bool
3.14       // float
5          // int
"a"        // str
"Hello world!" // str
'пуньк'    // str
0.         // float
0.0        // float
.0         // float
-3.14      // float
-12        // int
0x1a       // int
-0xffa3    // int


a = 10
b = 12
c = 42

val = (a == b or c - 12 == 30)
(a == b) or ((c - 12) == 30)
x or c - 12 == 30
x or y == 30
x or z
result

or --> bool
|
+---(==) --> bool
|     |
|     +--a
|     |
|     +--b
|
+---(==) --> bool
      |
      +--(-) --> int
      |   |
      |   +--c
      |   |
      |   +--12
      |
      +--30

-  бинарный оператор вычитания
== бинарный оператор логиеского сравнения на равенство
or бинарный оператор логического ИЛИ

or ||  False True
False  False True
True   True  True

and && False True
False  False False
True   False True

not !

a = 12

a == 12 --> True
(not (a == 12)) --> False
not a == 12 --> False
not a != 12 --> True

правила Де-Моргана
not (a or b) == not a and not b
not (a and b) == not a or not b

if expr:
    None
elif expr:
    None
elif expr:
    None
else:
    None
    
input() --> str
print() --> NoneType, None
"" + "" --> str, ""
bool()
int()
float()
str()


кортеж (tuple)
==============
[1, 2] - список int-ов ([int])
["ilya", "tanya"] - [str]

(1, "ilya") - кортеж из двух элеметов (int, str)
(42, "tanya")
("ilya", 1) - другой кортеж - (str, int)
() - пустой кортеж
(42, 1, 30) - (int, int, int)
return 33, "Jesus" - вернуть из функции кортеж

tpl = (42, "tanya")
print(tpl[0]) --> 42
a, b = tpm - распаковка кортежа

len(tpl) --> 2 - длина кортежа
len((3,4,5)) --> 3 - длина объявленного ad-hoc кортежа
len("ilya") --> 4 - длина строки
len([]) --> 0 - длина списка