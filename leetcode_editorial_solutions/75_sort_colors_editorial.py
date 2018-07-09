"""
Editorial one-pass solution.
runtime beats 100.00 % of python submissions.
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index = 0 
        two_index = len(nums) - 1
        i = 0
        while i < len(nums):
            if nums[i] == 2 and i < two_index:
                nums[i] = nums[two_index]
                nums[two_index] = 2
                two_index -= 1
                continue
            elif nums[i] == 0 and i > zero_index:
                nums[i] = nums[zero_index]
                nums[zero_index] = 0
                zero_index += 1
            else:
                i += 1