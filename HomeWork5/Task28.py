def sum(a, b):
    if b == 0:
        return a
    else:
        if b > 0:
            return sum(a + 1, b - 1)
        else:
            return sum(a - 1, b + 1)

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

print(sum(a,b))
