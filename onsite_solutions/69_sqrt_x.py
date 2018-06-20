
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left, right = 1, x
        while (right - left > 1):
            mid = (left + right) / 2
            if (mid * mid > x):
                right = mid
            else:
                left = mid
        return int(left)