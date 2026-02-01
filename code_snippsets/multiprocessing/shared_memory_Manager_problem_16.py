import multiprocessing


if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        d = manager.dict()
        d['list'] = [1, 2, 3]

        # {"list" : [1,2,3]}

        d['list'].append(4)
        #
        # temp = d['list']
        # temp.append(4)
        # d['list'] = temp  # Теперь изменения сохранены

        # # Способ 2: Вложенный прокси
        d['shared_list'] = manager.list([1, 2, 3])
        # {"shared_list" : [1,2,3]}
        d['shared_list'].append(4)  # ТАК РАБОТАЕТ, потому что это тоже прокси

        print(f"Dict: {d}")