"""
Onsite solution.
Time limit exceeded.
Fail case:
"acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb"
["abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd",
"ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c",
"cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa",
"bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc",
"acbccd","d","cccdcda","dcbd","cbccacd","ac","cca",
"aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca",
"abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"]
"""

class Solution(object):
    def is_word_break(self, s, words, max_len):
        """
        s: string
        words: set with words
        """
        if len(s) == 0:
            self.answer = True
        cur_string = ""
        for i in range(min(max_len, len(s))):
            cur_string += s[i]
            if cur_string in words:
                self.is_word_break(s[i+1:], words, max_len)
             
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(wordDict) == 0:
            return False
        self.answer = False
        max_len = len(max(wordDict, key=len))
        self.is_word_break(s, set(wordDict), max_len)
        return self.answer