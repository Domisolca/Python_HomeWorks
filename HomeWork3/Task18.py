import random

n = int(input('Введите количество элементов массива N: '))
m = []

for i in range(0, n):
    random_num = round(random.randint(1, n))
    m.append(random_num)
print(m)

x = int(input('Введите число X, для которого будем искать ближайший элемент: '))

if len(m) > 0:
    min = abs(x - m[0])
    result = m[0]
else:
    print('Массив пустой!')
    exit()


for i in m:
    diff = abs(x - i)
    if diff == min:
        if i < result:
            result = i
    elif diff < min:
        min = diff
        result = i

print(f'Минимальная разница = {min}')
print(f'Результат = {result}')