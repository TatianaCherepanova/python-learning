from os import system   #с помощью функции system мы запустим системную команду cls, которая очищает экран
import re


def genstub(word, oppened):
    rslt = ""
    count = 0   #переменная счётчик
    for letter in word:           # здесь in  часть синтаксиса цикла # перебираем буквы в слове
        if letter in oppened:     #in - специальный оператор, который проверяет есть ли элемент в списке
            rslt = rslt + letter
            count = count + 1   
        else:
            rslt = rslt + "*"
    return rslt, count  #кортеж, что примечательно без скобок


def is_valid(word):
    abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    if len(word) < 4:
        return False
    for letter in word:
        if letter not in abc:
            return False
    return True


word = input('Введите новое слово: ')
word = word.lower()
while not is_valid(word):
    word = input('Введите новое слово. Используйте буквы русского языка!: ')
    word = word.lower()


system('cls')

abc = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
oppened = []    #пустой список
totalattempts = 10
attempts = totalattempts

stub, num = genstub(word, oppened)  # распаковка кортежа
while attempts != 0 and num != len(word):   # функция len возвращает длину последовательности
    # код ниже выполняется в цикле до тех пор пока не
    # истечет доступное количество попыток или пока слово не будет
    # угадано. 
    letter = input("Угадайте букву в слове " + stub + " У вас осталось " + str(attempts) + " попыток: ")    #str(attempts) конвертация типа int в str
    letter = letter.lower()
    # валидируем символ; если символ валиден, проверяем есть
    # ли он в строке (с помощью уже знакомого нам оператора in)
    
    if len(letter) != 1:
        print("Вводите одну букву")
    elif letter not in abc:
        print("Вводите букву кириллицей")
    elif letter in word:
        # если символ найден, добавить в список открытых символов и
        # вывести на экран сообщение "есть такая буква"
        print("ЕСТЬ ТАКАЯ БУКВА!")
        oppened.append(letter)    #добавить в конец списка новый элемент. Метод append добавляет элемент в конец списка
    else:
        # в противном случае уменьшить количество попыток, вывести
        # на экран сообщение об ошибке "нет такой буквы в этом слове"
        print("Не угадал")
        attempts = attempts - 1

    stub, num = genstub(word, oppened)


if attempts != 0:
    assert(num == len(word))    #assert проверка правильности 
    print("ПОЗДРАВЛЯЮ! Вы угадали слово " + word.upper() + " за " + str(totalattempts - attempts + len(oppened)) + " попыток") 
else:
    assert(num != len(word))
    print("Сожалею, но вы проиграли. Попробуйте заново.")



 
