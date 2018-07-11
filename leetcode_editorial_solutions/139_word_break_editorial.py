"""
Beats 99.6% of all python solutions.
"""

class Solution(object):
    """
    Idea: break each substring into two and check for both using DP
    """
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        memo = [False] * (len(s)+1)
        memo[0] = True # null string
        for i in range(1, len(s)+1):
            for j in range(i):
                if memo[j] and s[j:i] in wordDict:
                    memo[i] = True
                    break
        return memo[-1]
