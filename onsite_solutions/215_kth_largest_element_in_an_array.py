"""
O(n * log k) time
O(k) space

"""

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k_heap = []
        for i in range(len(nums)):
            if i < k:
                heapq.heappush(k_heap, nums[i])
            else:
                heapq.heappush(k_heap, max(nums[i], heapq.heappop(k_heap)))
        return heapq.heappop(k_heap)

       