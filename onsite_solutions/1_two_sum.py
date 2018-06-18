class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = dict()
        for i, value in enumerate(nums):
            if target - value in indices:
                return [indices[target - value], i]
            indices[value] = i