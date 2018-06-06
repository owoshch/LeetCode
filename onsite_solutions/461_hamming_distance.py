"""
9 minutes.
Beats 91.25 % of python3 submissions.
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count("1")