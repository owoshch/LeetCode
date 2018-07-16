"""
Two passes solution.
Runtime beats 99.47 % of python submissions
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        output = []
        for i in range(len(nums)):
            output.append(product)
            product *=  nums[i]
        product = 1
        for i in range(len(output) - 1, -1, -1):
            output[i] *= product
            product *= nums[i]
        return output