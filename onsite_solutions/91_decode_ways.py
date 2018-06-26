"""
22 minutes. Accepted.
Runtime beats 34.77 % of python submissions
"""


class Solution(object):
    def count_decodings(self, s, memo):
        if memo[len(s)] != -1:
            return memo[len(s)]
        number_of_ways = 0
        if int(s[-1:]) > 0 and len(s) - 1 >= 0:
            number_of_ways += self.count_decodings(s[:-1], memo) 
        if 10 <= int(s[-2:]) <= 26 and len(s) - 2 >= 0:
            number_of_ways += self.count_decodings(s[:-2], memo) 
        memo[len(s)] = number_of_ways
        return memo[len(s)]
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = [-1] * (len(s) + 1)
        memo[0] = 1
        return self.count_decodings(s, memo)