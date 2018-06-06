"""
Accepted.
Runtime beats 97.69 % of python3 submissions.
"""

class Solution:    
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        """
        Iterate though both the array and 
        copy max element to n + m - 1 position in nums1
        until one of them runs out of items
        """
        while (m > 0 and n > 0):
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        # write the remaining items
        while m > 0:
            nums1[m + n - 1] = nums1[m - 1]
            m -=1
        while n > 0:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1