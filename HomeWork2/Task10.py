import random
n = int(input('Введите количество монеток n: '))
m = []
count_0 = 0
count_1 = 0
for i in range(0, n):
    random_num = round(random.randint(0, 1))
    m.append(random_num)
    if m[i] == 0 : count_0 += 1
    else : count_1 += 1

print(m)

if count_0 >= count_1: print(count_1)
else: print(count_0)