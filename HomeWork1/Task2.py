n = int(input('Введите трехзначное число = '))

if n >= 100 and n <= 999:
    n3 = n % 10
    n = n // 10
    n2 = n % 10
    n1 = n // 10

    print(n3 + n2 + n1)
else:
    print('Число не трехзначное!')