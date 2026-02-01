from multiprocessing import Process, Manager

def fill_dict(shared_dict, shared_list, common_lst):
    shared_dict["status"] = "Success"
    shared_list.append("Новый элемент")
    common_lst.append("Append from another process")

if __name__ == "__main__":
    with Manager() as manager:
        # Создаем структуры через менеджер
        shared_dict = manager.dict()
        shared_list = manager.list([1, 2])
        common_lst = []

        p = Process(target=fill_dict, args=(shared_dict, shared_list, common_lst))
        p.start()
        p.join()

        print(f"Словарь: {shared_dict}")
        print(f"Список: {shared_list}")
        print(f"Regular list: {common_lst}")