my_list = [5, 1, 4, 2, 8, 4, 0, 3, 2]

def bubble_sort(arr):
    lenght = len(arr)
    for i in range(lenght - 1):
        for j in range(lenght - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(i)
    return arr

def bubble_sort_optimized(arr):
    lenght = len(arr)
    for i in range(lenght - 1):
        swaped = False
        for j in range(lenght - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaped = True
        if not swaped:
            print(f'{i}: {swaped}')
            break
    return arr    

print(bubble_sort(my_list))
print()
print(bubble_sort_optimized(my_list))
