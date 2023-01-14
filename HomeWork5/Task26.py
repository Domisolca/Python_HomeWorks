def power(a,b):
    if b == 0:
        return 1
    if b < 0:
        return 1/power(a, -b)
    return a * power(a, b-1)

a = int(input('Введите число a: '))
b = int(input('Введите степень b: '))

print(power(a,b))