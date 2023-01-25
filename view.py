def get_oper():
    op = int(input(' 1 - добавить пользователя \n 2 - вывести таблицу \n 3 - вывести имя и фамилию \n 4 - отсортировать по имени \n 5 - отсортировать по id \n 6 - выход \n'))
    return op

def add_worker():
    id = input('Введите ID: ')
    name = input('Введите имя: ')
    lastname = input('Введите фамилию: ')
    number = input('Введите номер телефона: ')
    comments = input('Введите комментарий: ')
    line = f'{id},{name},{lastname},{number},{comments}\n'
    with open ("worker_list.txt", "a") as file:
        file.write(line)
    print('Сохранено!')

def print_table():
    with open ("worker_list.txt", "r") as file:
        for line in file.readlines():
            print(line, end="")

def print_name():
    with open ("worker_list.txt", "r") as file:
        lst = file.readlines()
        for line in lst:
            a = line.split(",")
            print(f'Имя - {a[1]}, Фамилия - {a[2]}')

def sort_names():
    with open ("worker_list.txt", "r") as file:
        lst = file.readlines()
        lst_with_lst = []
        for line in lst:
            if line != "\n":
                a = line.split(",")
                lst_with_lst.append(a)

        lst_with_lst = sorted(lst_with_lst, key = lambda x: x[1])
        string_ = ""
        for worker in lst_with_lst:
            res = ",".join(worker)
            string_ += res + "\n"
    with open ("worker_list.txt", "w") as file:
        file.write(string_)

def sort_id():
    with open ("worker_list.txt", "r") as file:
        lst = file.readlines()
        lst_with_lst = []
        for line in lst:
            if line != "\n":
                a = line.split(",")
                lst_with_lst.append(a)

        lst_with_lst = sorted(lst_with_lst, key = lambda x: x[0])
        string_ = ""
        for worker in lst_with_lst:
            res = ",".join(worker)
            string_ += res + "\n"
    with open ("worker_list.txt", "w") as file:
        file.write(string_)