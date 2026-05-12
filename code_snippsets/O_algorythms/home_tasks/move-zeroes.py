# https://leetcode.com/problems/move-zeroes/description/
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveZeroes(n: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = 0
    for i in range(len(nums)):
        if n[i] != 0:
            n[i], n[left]  = n[left], n[i]
            left += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)

