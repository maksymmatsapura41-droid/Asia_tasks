def partition(arr, low, high):
    pivot = arr[high] # value, not index
    i = low - 1 # index,  -1 for first element in array
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1 # index for moved pivot

def quick_sort(arr, low, high):
    # low - index, high - index
    if low < high: 
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    
arr = [7, 2, 1, 6, 8, 5, 3]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
    
