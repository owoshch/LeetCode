class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        
    The general idea is to iterate over string s.
    Always put the character c and its location i in the dictionary d.
    1) If the sliding window contains less than or equal to k distinct characters, simply record the return value, and move on.
    2) Otherwise, we need to remove a character from the sliding window.
       Here's how to find the character to be removed:
       Because the values in d represents the rightmost location of each character in the sliding window, in order to find the longest substring T, we need to locate the smallest location, and remove it from the dictionary, and then record the return value.
        """
        characters = {}
        low, ret = 0, 0
        for i, char in enumerate(s):
            characters[char] = i
            if len(characters) > k :
                low = min(characters.values())
                del characters[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret
