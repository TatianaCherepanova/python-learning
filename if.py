number = 23
guess = int(input("Введите целое число: "))

if guess == number:
    print("Congratulations!" )
elif guess < number:
    print("No, number is bigger then that")
else:
    print("No, number is smaller then that")