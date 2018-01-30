class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                max_len = max(max_len, i - left + 1)
            else:
                left = i + 1
        return max_len
            
