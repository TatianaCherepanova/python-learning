number = 23
running = True

while running:
    guess = int(input('введите enter an integer: '))

    if guess == number:
        print('Congratulations!')
        running = False
    elif guess < number:
        print('Wrong, the specified number is greater.')
    else:
        print('Wrong, the specified number is less.')

#else:
    #print('while')

print('Finish!')