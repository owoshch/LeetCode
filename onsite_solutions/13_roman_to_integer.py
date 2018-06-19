class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        r2i = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "B": 10000}
        s = "B" + s
        i = len(s) - 1
        while i > 0:
            if r2i[s[i]] > r2i[s[i - 1]]:
                result += (r2i[s[i]] - r2i[s[i - 1]])
                i -= 2
            else:
                result += r2i[s[i]]
                i -= 1
        return result
        