
# https://leetcode.com/problems/3sum
# 15. 3Sum
class Solution(object):
    def threeSum(self, nums):
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        return result
    
# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        for i in range(1, len(nums)):
            if nums[left] != nums[i]:
                left += 1
                nums[left] = nums[i]
        return left


