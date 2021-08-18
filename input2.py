from os import system  # с помощью функции system мы запустим системную команду cls, которая очищает экран
import re


def genstub(word, oppened):
    rslt = ""
    count = 0  # переменная счётчик
    for letter in word:  # здесь in  часть синтаксиса цикла # перебираем буквы в слове
        if letter in oppened:  # in - специальный оператор, который проверяет есть ли элемент в списке
            rslt = rslt + letter
            count = count + 1
        else:
            rslt = rslt + "*"
    return rslt, count  # кортеж, что примечательно без скобок


word = input('Введите новое слово: ')
system('cls')

abc = (
    "а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я А Б В Г Д Е Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я").split()
oppened = []  # пустой список
totalattempts = 10
attempts = totalattempts

stub, num = genstub(word, oppened)  # распаковка кортежа
while attempts != 0 and num != len(word):  # функция len возвращает длину последовательности
    # TODO: код ниже должен выполняться в цикле до тех пор пока не
    # истечет доступное количество попыток или пока слово не будет
    # угадано. Использовать цикл while
    letter = input("Угадайте букву в слове " + stub + " У вас осталось " + str(
        attempts) + " попыток: ")  # str(attempts) конвертация типа int в str
    # TODO: валидировать символ; если символ валиден, проверить есть
    # ли он в строке (с помощью уже знакомого нам оператора in)

    # ФУНКЦИЯ валидации, которая принимает letter и возвращает  true/false

    if letter not in abc:
        print("Вводите букву кириллицей")

    if letter in word:
        # если символ наден, добавить в список открытых символов и
        # вывести на экран сообщение "есть такая буква"
        print("ЕСТЬ ТАКАЯ БУКВА!")
        oppened.append(letter)  # добавить в конец списка новый элемент. Метод append добавляет элемент в конец списка
    else:
        # в противном случае уменьшить количество попыток, вывести
        # на экран сообщение об ошибке "нет такой буквы в этом слове"
        print("Не угадал")
        attempts = attempts - 1

    stub, num = genstub(word, oppened)

if attempts != 0:
    assert (num == len(word))  # assert проверка правильности
    print("ПОЗДРАВЛЯЮ! Вы угадали слово " + word.upper() + " за " + str(
        totalattempts - attempts + len(oppened)) + " попыток")
else:
    assert (num != len(word))
    print("Сожалею, но вы проиграли. Попробуйте заново.")


