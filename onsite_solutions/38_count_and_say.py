"""
Runtime beats 59.56 % of python submissions.
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for i in range(1, n):
            temp = ""
            counter = 1
            result += "_"
            for i in range(len(result)):
                if i >= len(result) - 1 or result[i] == result[i + 1]:
                    counter += 1
                else:
                    temp += str(counter) + result[i]
                    counter = 1
            result = temp
        return result
        