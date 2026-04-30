
# https://leetcode.com/problems/3sum
# 15. 3Sum
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    if [nums[i], nums[left], nums[right]] not in result:
                        result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
        return result
    
# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        k = 1
        for i in range(1, len(nums)):
            if nums[left] != nums[i]:
                left += 1
                nums[left] = nums[i]
                k += 1
        return k  
