# two pointers technique, same as my idea, more smart tracking of min lenght
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = float("inf")
        left = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            while (cur_sum >= s):
                ans = min(ans, i + 1 - left)
                cur_sum -= nums[left]
                left += 1
        if ans == float("inf"):
            return 0
        else:
            return ans
