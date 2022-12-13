n = int(input('Введите n = '))
m = int(input('Введите m = '))
k = int(input('Введите k = '))

if n * m > k:
    if k % n == 0 or k % m == 0:
        print('yes')
    else:
        print('no')
else:
    print('no')