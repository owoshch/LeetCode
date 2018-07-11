"""
Onsite solution 2.
Time limit exceeded.
Fail case:
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]


class Solution(object):
    def is_word_break(self, s, words, max_len, is_found):
        """
        s: string
        words: set with words
        """
        if len(s) == 0:
            return True
        cur_string = ""
        for i in range(min(max_len, len(s))):
            cur_string += s[i]
            if cur_string in words:
                if self.is_word_break(s[i+1:], words, max_len, is_found):
                    return True
        return False
             
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(wordDict) == 0:
            return False
        max_len = len(max(wordDict, key=len))
        return self.is_word_break(s, set(wordDict), max_len, False)
