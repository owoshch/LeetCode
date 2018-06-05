"""
25 minutes.
Doesn't pass the tests. However, for me it returns the correct output on all test cases.
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        length = len(nums)
        i, j = 0, 0
        while j < length:
            print (j, length)
            if nums[i] == nums[j]:
                j += 1
            else: # now nums[i] != nums[j]
                nums = nums[:i+1] + nums[j:]
                length = length - (j - i) + 1
                i = i + 1
                j = i
        length = length - (j - i) + 1
        return length
        