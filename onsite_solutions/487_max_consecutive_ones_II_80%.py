class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        left_first, left_second = 0, 0
        max_len = 0
        for right, element in enumerate(nums):
            if element == 0:
                max_len = max(max_len, right - left_first)
                left_first, left_second = left_second, right + 1
        return max_len
        
                
        