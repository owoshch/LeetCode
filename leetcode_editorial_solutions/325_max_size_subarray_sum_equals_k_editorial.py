class Solution:
    def maxSubArrayLen(self, nums, k):
        # O(n) solution using hash map
        answer = 0
        accumulative_sum = 0
        partial_sums = {0: -1} #dict {accum_sum : index}
        for i in range(len(nums)):
            accumulative_sum += nums[i]
            if accumulative_sum not in partial_sums:
                partial_sums[accumulative_sum] = i
            if accumulative_sum - k in partial_sums:
                answer = max(answer, i - partial_sums[accumulative_sum - k])
        return answer