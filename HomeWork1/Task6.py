s = input('Введите шетизначный номер билета = ')
if len(s) == 6:
    left_part = int(s[0]) + int(s[1]) + int(s[2])
    right_part = int(s[3]) + int(s[4]) + int(s[5])
    if left_part == right_part:
        print('yes')
    else:
        print('no')
else:
    print('Номер должен состоять из 6 знаков')