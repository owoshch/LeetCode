"""

My O(n2) solution. However, its still exceeds time limit

"""


class Solution:
    def _search(self, nums, value):
        # search from 0 to len(nums) - 1
        # for two numbers summing up to value
        pairs = []
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < value:
                left += 1
            elif nums[left] + nums[right] > value:
                right -= 1
            else:
                pairs.append([nums[left], nums[right]])
                left += 1
                right -= 1
        if len(pairs):
            return pairs
        return []
            
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
        1) Sort the arr, O(nlogn)
        2) for each element in the arr 
        try to find two elements that sum up to -element
        n^2 instead of brute force n^3
        
        """
        results = []
        nums.sort()
        for i in range(len(nums)):
            triplet = []
            pairs = self._search(nums[i + 1:], -nums[i])
            for left, right in pairs:
                if left != None and right != None:
                    # found the pair
                    triplet = [nums[i], left, right]
                if len(triplet) == 3:
                    if triplet not in results:
                        results.append(triplet)
        return results