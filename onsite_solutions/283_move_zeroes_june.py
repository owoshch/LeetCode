"""
Move zeroes, June 7, 25 minutes
Runtime beats 5.78 % of python3 submissions.
That's sad though. Keep practicing.
"""


class Solution:  
    def swipe(self, arr, left, right):
        memo = arr[right]
        arr[right] = arr[left]
        arr[left] = memo
        return memo
    def shift_left(self, arr, left, right):
        for i in range(left, right):
            arr[i] = arr[i + 1]
             
    def moveZeroes(self, arr):
        """
        1) left, right indices
        2) swipe(left, right) if arr[left] == 0 and
        memorize right
        3) shift arr[left:right] one step left
        4) left += 1, right -= 1
        5) repeat while left < right
        """
        if len(arr) == 0:
            return arr
        left, right = 0, len(arr) - 1
        while left < right:
            while right > 0 and arr[right] == 0:
                right -= 1
            if arr[left] == 0:
                memo = self.swipe(arr, left, right)
                self.shift_left(arr, left, right)
                right -= 1
                arr[right] = memo
            else:
                left += 1