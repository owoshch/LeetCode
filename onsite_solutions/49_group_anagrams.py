"""
Time limit exceeded.
"""


class Solution(object):
    def count_letters(self, word):
        word_dict = {}
        for letter in word:
            if letter in word_dict:
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1
        return word_dict
    
    def anagram_exists(self, result, word):
        for i, arr in enumerate(result):
            if self.count_letters(arr[0]) == self.count_letters(word):
                return i
        return -1
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        for word in strs:
            index = self.anagram_exists(result, word)
            if not result or index == -1:
                result.append([word])
            else:
                result[index].append(word)
        return result
                