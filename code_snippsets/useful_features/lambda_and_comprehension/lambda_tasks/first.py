# Find negative numbers and replace them with zero
nums = [3, -1, 0, 7, -5, -10, 12]
print(list(map(lambda x: 0 if x < 0 else x, nums)))

