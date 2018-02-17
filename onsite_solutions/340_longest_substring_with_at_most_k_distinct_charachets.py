#Time limit exceeded

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == k:
            return len(s)
        
        max_len = 0
        for i in range(len(s)):
            j = i
            alphabet = set()
            while j < len(s) and len(alphabet) <= k:
                if s[j] not in alphabet:
                    alphabet.add(s[j])
                if len(alphabet) <= k:
                    j += 1
            max_len = max(max_len, j - i)
        return max_len