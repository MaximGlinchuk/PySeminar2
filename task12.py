summa = int(input('Сумма чисел равна: '))
multi = int(input('Произведение чисел: '))
result = False
for i in range(0,1000):
    for j in range(0,1000):
        if i + j == summa and i * j == multi:
            print(f'Петя загадал: {i},{j}')
        else:
            i += 1
            j += 1