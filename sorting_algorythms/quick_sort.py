def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = nums[len(nums) // 2] # value!

    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

arr = [7, 2, 1, 6, 8, 5, 3]
print(quick_sort(arr))
    
