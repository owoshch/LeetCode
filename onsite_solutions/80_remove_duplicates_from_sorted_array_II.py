"""
26 minutes
Runtime beats 19.59 % of python3 submissions.

"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i, j = 0, 0
        max_len = len(nums)
        while j < max_len:
            while j < max_len and nums[j] == nums[i]:
                j += 1
            if j - i >= 2:
                i += 2
                diff = j - i
                # move the rest of the array to the left
                swap_index = i
                while j < max_len:
                    nums[swap_index] = nums[j]
                    swap_index += 1
                    j += 1
                max_len -= diff
                j = i
            else:
                # we did just one step
                i = j
        return max_len
            
            
        