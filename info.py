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

# print -- 'это функция (комментарии). Текст программы говорит о том, КАК,
# а комментарии должны объяснять, ПОЧЕМУ
#Литеральные константы - Они называются литеральными, потому что их значение используется буквально.
5, 1.23, 9.25e-3 или 'Это строка' или "It's a string!"

Числа
2 - целое цисло
3.23, 2.3E-4 - с плавающей точкой (Е - показывает степень числа 10)
(-5+4j) и (2.3 - 4.6j) комплексные

Строка – это последовательность символов. Чаще всего строки – это просто некоторые
наборы слов. По умолчанию все строки в Unicode.

Одинарные кавычки
Строку можно указать, используя одинарные кавычки, как например, 
'Фраза в кавычках'. Все пробелы и знаки табуляции сохранятся, как есть.

Двойные кавычки
Строки в двойных кавычках работают точно так же, как и в одинарных. Например,
"What's your name?".

Тройные кавычки
Можно указывать «многострочные» строки с использованием тройных кавычек 
(""" или'''). 
В пределах тройных кавычек можно свободно использовать одинарные и двойные кавычки. 
Например:
'''Это многострочная строка. Это её первая строка.
Это её вторая строка.
"What's your name?", - спросил я.
Он ответил: "Bond, James Bond."
'''

Строки неизменяемы! Это означает, что после создания строки её больше нельзя изменять.

Объединение строковых констант
'What\'s ' 'your name?' автоматически преобразуется в "What's your name?"

Метод format
Иногда бывает нужно составить строку на основе каких-либо данных.
Детально такие обозначения форматов описаны в Предложении по расширению Python PEP 3101.

age = 26
name = 'Swaroop'

print('Возраст {} -- {} лет.'.format(name, age))
print('Почему {} забавляется с этим Python?'.format(name))

>>> # десятичное число (.) с точностью в 3 знака для плавающих:
>>> '{0:.3}'.format(1/3)
'0.333'
>>> # заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
>>> '{0:_^11}'.format('hello')
'___hello___'
>>> # по ключевым словам:
>>> '{name} написал {book}'.format(name='Swaroop', book='A Byte of Python')
'Swaroop написал A Byte of Python'

Переменные
Слово «переменные» говорит само за себя – их значение может
меняться, а значит, вы можете хранить в переменной всё, что угодно.

Имена идентификаторов
Переменные – это частный случай идентификаторов. Идентификаторы – это имена, при-
своенные чему-то для его обозначения. При выборе имён для идентификаторов необхо-
димо соблюдать следующие правила:
• Первым символом идентификатора должна быть буква из алфавита (символ ASCII в
верхнем или нижнем регистре, или символ Unicode), а также символ подчёркивания
(«_»).
• Остальная часть идентификатора может состоять из букв (символы ASCII в верхнем
или нижнем регистре, а также символы Unicode), знаков подчёркивания («_») или
цифр (0-9).
• Имена идентификаторов чувствительны к регистру. Например, myname и myName –
это не одно и то же. Обратите внимание на «n» в нижнем регистре в первом случае
и «N» в верхнем во втором.
• Примеры допустимых имён идентификаторов: i, __my_name, name_23, a1b2_c3 и
любые_символы_utf8_δξѪђёўЩӆΞέά.
• Примеры недопустимых имён идентификаторов: 2things, здесь есть пробелы,
my-name, >a1b2_c3 и "это_в_кавычках".

Типы данных
Переменные могут хранить значения разных типов, называемых типами данных. 

Объекты
Помните, Python рассматривает всё, что есть в программе, как объекты. Имеется в виду, в
самом общем смысле. Вместо того, чтобы говорить «нечто», мы говорим «объект».


Использование переменных и констант
# Имя файла : var.py
i = 5
print(i)
i = i + 1
print(i)
s = '''Это многострочная строка.
Это вторая её строчка.'''
print(s)
Вот как эта программа работает. Сперва мы присваиваем значение констан-
ты 5 переменной i, используя оператор присваивания (=). Эта строка назы-
вается предложением и указывает, что должно быть произведено некоторое
действие, и в данном случае мы связываем имя переменной i со значением
5. Затем мы печатаем значение i, используя функцию print, которая просто
печатает значение переменной на экране.
7.8. Объекты 42
A Byte of Python (Russian), Версия 2.02
Далее мы добавляем 1 к значению, хранящемуся в i и сохраняем его там. По-
сле этого мы печатаем его и получаем значение 6, что неудивительно.
Аналогичным образом мы присваиваем строковую константу переменной s,
после чего печатаем её.

