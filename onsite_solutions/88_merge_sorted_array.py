"""
20 minutes.
Doesn't work: time limit exceeded.
"""


class Solution:
    def insert(self, nums1, i, nums2, j):
        for index_to_shift in range(len(nums1) - 1, i, -1):
            nums1[index_to_shift] = nums1[index_to_shift - 1]
        nums1[i] = nums2[j]
        
    
    
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        i, j, seen_first = 0, 0, 0
        while j < n and seen_first < m:
            if nums1[i] <= nums2[j]:
                i += 1
                seen_first += 1
            else:
                # instert nums2[j] at ith position
                self.insert(nums1, i, nums2, j)
                i += 1
                j += 1
        if j < n:
            nums1[i:] = nums2[j:]
        return
        