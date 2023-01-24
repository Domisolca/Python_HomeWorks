n = '22 * 300 / 7 - 14 + 10 * 10 * 10 + 20 * 2 / 3'

m = n.split()
m2 = []
m3 = []

print(m)


def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b

result = float(m[0])

past_op = ''

for i in range(1, len(m) - 1, 2):
    if (m[i] == '*' or m[i] == '/') and (past_op == ''):
        result = calc(float(m[i - 1]), float(m[i + 1]), m[i])
        m2.append(result)
        past_op = m[i]
    elif (m[i] == '*' or m[i] == '/') and (past_op != ''):
        result = calc(result, float(m[i + 1]), m[i])
        m2.pop(-1)
        m2.append(result)
        past_op = m[i]
    else:
        m2.append(m[i])
        m2.append(float(m[i + 1]))
        past_op = ''

past_digit = ''

for i in m2:
    if i == '+' or i == '-':
        m3.append(i)
        past_digit = ''
    elif past_digit == '':
        m3.append(i)
        past_digit = i
    else:
        m3.pop(-1)
        m3.append(i)
        past_digit = ''

print(m2)
print(m3)

result = float(m3[0])

for i in range(1, len(m3) - 1, 2):
    result = calc(result, float(m3[i + 1]), m3[i])

print(result)