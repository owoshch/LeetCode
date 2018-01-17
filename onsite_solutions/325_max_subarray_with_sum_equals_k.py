# O(n!) time complexity
# In 20 minutes didn't come up with O(n) solution
# Editorial O(n) solution implemented by me can be found in another folder
class Solution:
	def maxSubArrayLen(self, nums, k):
		# time limit exceeded solution
        	window_size = len(nums)
        	i = 0
        	while window_size > 0:
            		for i in range(len(nums) - window_size + 1):
                		cur_sum = sum(nums[i: i + window_size])
                		if cur_sum == k:
                    			return window_size
            		window_size -= 1
        	return 0
