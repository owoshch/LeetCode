class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        left = 0
        right = 0
        max_len = 0
        for right, element in enumerate(nums):
            if element == 0:
                max_len = max(max_len, right - left)
                left = right + 1
        return max_len