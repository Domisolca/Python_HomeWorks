def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result

def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list +'\n')


def print_bus():
    return read_data_from_file('bus.txt')

def add_bus():
    save_data_to_file('bus.txt', input("Введите параметры автобуса: "))
    
def print_driver():
    return read_data_from_file('driver.txt')

def add_driver():
    save_data_to_file('driver.txt', input("Введите водителя: "))

def print_route():
    return read_data_from_file('route.txt')

def add_route():
    save_data_to_file('route.txt', input("Введите маршрут: "))

def print_item(item, items):
    result = "Not found"
    for i in items:
        if i[0] == item:
            result = i[1]
    return result

def rout_detalization():
    routes = read_data_from_file('route.txt')
    bus = read_data_from_file('bus.txt')
    driver = read_data_from_file('driver.txt')
    for route in routes:
        print("Номер маршрута: " + route[1] + ", номер автобуса: " + print_item(route[2], bus)+ ", фамилия водителя: " + print_item(route[3], driver))