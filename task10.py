import random

n = int(input('Введите колличество монеток: '))
count_one = 0
count_zero = 0
i = 1
while i <= n:
    money = random.randint(0, 1)
    if money == 0:
        count_zero += 1
    else:
        count_one += 1
    i += 1
    print(money)
if count_one > count_zero:
    print(f'Необходимо перевернуть монеток: {count_zero}')
else:
    print(f'Необходимо перевернуть монеток: {count_one}')