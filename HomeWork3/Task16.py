import random
n = int(input('Введите количество элементов массива N: '))
m = []

for i in range(0, n):
    random_num = round(random.randint(1, n//2))
    m.append(random_num)
print(m)

x = int(input('Введите число для поиска X: '))

count = 0

for i in range(0, len(m)):
    if m[i] == x:
        count+=1

print(f'{x} встречается в массиве {count} раз')