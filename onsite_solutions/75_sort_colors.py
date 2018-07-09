"""
Two pass solution.
Runtime beats 98.48 % of python submissions.
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        counter = {0: 0, 1:0, 2:0}
        for number in nums:
            counter[number] += 1
        nums[:counter[0]] = [0] * counter[0]
        nums[counter[0]: counter[0] + counter[1]] = [1] * (counter[1])
        nums[counter[0] + counter[1]:] = [2] * (counter[2])