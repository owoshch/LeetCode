"""
Runtime beats 100.00 % of python submissions
"""

class Solution(object):
    def generate_subsets(self, powerset, temp, nums, start):
        powerset.append(temp)
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                # skip duplicates
                continue
            self.generate_subsets(powerset, temp + [nums[i]], nums, i+1)
    
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        powerset = []
        nums.sort()
        self.generate_subsets(powerset, [], nums, 0)
        return powerset