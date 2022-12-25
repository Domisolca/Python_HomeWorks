import random

n = int(input('Введите количество элементов массива n: '))
x = []

for i in range(0, n):
    random_num = round(random.randint(1, 20))
    x.append(random_num)
print(x)

m = int(input('Введите количество элементов массива m: '))
y = []

for i in range(0, m):
    random_num = round(random.randint(1, 20))
    y.append(random_num)
print(y)

z = set(x)&set(y)

print(sorted(z))