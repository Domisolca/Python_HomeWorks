s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))

flag = False
for i in range(s):
    if flag:
        break
    for j in range(s):
        if i + j == s and i * j == p:
            flag = True
            print(i, j)
            break
if not flag:
    print('Таких натуральных чисел нет!')