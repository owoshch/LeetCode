"""
June, 11
20 minutes, wrong answer in the case when the first string has one symbol in it:
s = "a"
t = "aa"
"""


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        indices = [-1, -1]
        min_len = float('inf')
        substing_dict = dict(zip(set(t), [-1] * len(set(t))))
        found_letters = set([])
        for i, letter in enumerate(s):
            if letter in set(t):
                found_letters.add(letter)
                if substing_dict[letter] < i:
                    substing_dict[letter] = i
                    if len(found_letters) == len(set(t)):
                        distance = max(substing_dict.values()) - min(substing_dict.values())
                        if min_len > distance:
                            indices[0] = min(substing_dict.values())
                            indices[1] = max(substing_dict.values())
                            min_len = distance
        if -1 not in indices:
            return s[indices[0]: indices[1] + 1]
        else:
            return ""