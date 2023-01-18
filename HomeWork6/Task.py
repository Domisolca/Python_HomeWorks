fileName = 'tel.txt'


def writeFile(file_name, fio, phone):
    with open(file_name, 'a') as data:
        data.writelines(fio + "," + phone + '\n')


def readFile(file_name):
    result = []
    with open(file_name, 'r+') as data:
        for line in data:
            result.append(line.split(','))
        return result


def findUsers(userList, name):

    for user in userList:
        if user[1] == name:
            print("Телефон: " + user[3])

def showRecords(file_name):
    rec_list = readFile(file_name)
    for rec in rec_list:
        print(rec[0]+ " " + rec[1]+ " " + rec[2]+ " " + rec[3])

def findUserByPhone(userList, phone):

    for user in userList:
        if user[3] == phone+'\n':
            print(user[0]+ " " + user[1]+ " " + user[2]+ " " + user[3])

def deleteContactByPhone(userList, file_name, phone):
    with open(file_name, 'w') as data:
        for user in userList:
            if user[3] != phone+'\n':
                data.writelines(user[0]+ "," + user[1]+ "," + user[2]+ "," + user[3])

def replaceContactPhone(userList, file_name, phone1, phone2):
    with open(file_name, 'w') as data:
        for user in userList:
            if user[3] == phone1+'\n':
                data.writelines(user[0]+ "," + user[1]+ "," + user[2]+ "," + phone2+'\n')
            else:
                data.writelines(user[0]+ "," + user[1]+ "," + user[2]+ "," + user[3])

while(True):
    n = int(input("Введите номер действия:\n1 - Показать все записи\n2 - Найти запись по вхождению частей имени\n3 - Найти запись по телефону\n4 - Добавить новый контакт\n5 - Удалить контакт\n6 - Изменить номер телефона у контакта\n7 - Выход\n>>>"))
    if n == 7:
        break
    elif n == 1:
        showRecords(fileName)
    elif n == 2:
        name = input("Введите Имя для поиска: ")
        findUsers(readFile(fileName), name)
    elif n == 3:
        phone = input("Введите Телефон для поиска: ")
        findUserByPhone(readFile(fileName), phone)
    elif n == 4:
        f = input("Введите Фамилию: ")
        i = input("Введите Имя: ")
        o = input("Введите Отчество: ")
        phone = input("Введите Телефон: ")
        writeFile(fileName, f+','+i+','+o, phone)
    elif n == 5:
        phone = input("Введите Телефон для удаления: ")
        deleteContactByPhone(readFile(fileName),fileName, phone)
    elif n == 6:
        phone1 = input("Введите Телефон для поиска контакта: ")
        phone2 = input("Введите Телефон, на который заменить: ")
        replaceContactPhone(readFile(fileName),fileName, phone1, phone2)