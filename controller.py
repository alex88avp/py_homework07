import view

def start():
    while True:
        op = view.get_oper()
        if op == 1:
            view.add_worker()
        elif op == 2:
            view.print_table()
        elif op == 3:
            view.print_name()
        elif op == 4:
            view.sort_names()
        elif op == 5:
            view.sort_id()
        elif op == 6:
            break