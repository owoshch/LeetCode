"""
O(N) guaranteed running time + O(1) space
The smart approach for this problem is to use the selection algorithm 
(based on the partion method - the same one as used in quicksort).
So how can we improve the above solution and make it O(N) guaranteed? 
To make the solution O(N) guaranteed we can randomize the input, so that even when 
the worst case input would be provided the algorithm wouldn't be affected. 
So all what it is needed to be done is to shuffle the input.
"""


class Solution:
    def findKthLargest(self, nums, k):
        # convert the kth largest to smallest
        random.shuffle(nums)
        return self.findKthSmallest(nums, len(nums)+1-k)
    
    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos+1:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot   
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low


        