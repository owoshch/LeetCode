class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        zero_left = 0
        zero_right = 0
        for i in range(len(nums)):
            zero_right += 1
            if nums[i] == 0:
                zero_left = zero_right
                zero_right = 0
            max_len = max(max_len, zero_left + zero_right)
        return max_len
