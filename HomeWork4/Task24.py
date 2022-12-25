import random

n = int(input('Введите количество кустов: '))
x = []

for i in range(0, n):
    random_num = round(random.randint(1, 10))
    x.append(random_num)
print(x)

if len(x) >= 3:
    x.insert(0,x[-1])
    x.insert(len(x), x[1])

    max = x[1] + x[0] + x[2]
    for i in range(2, len(x)-1):
        if x[i] + x[i-1] + x[i+1] > max:
            max = x[i] + x[i-1] + x[i+1]
    print(f'Результат = {max}')
elif len(x) == 2:
    print(f'Результат = {x[0]+x[1]}')
elif len(x) == 1:
    print(f'Результат = {x[0]}')
else:
    print('Нет кустов для сбора!')