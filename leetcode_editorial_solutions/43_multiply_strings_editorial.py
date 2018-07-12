"""
Multiply strings.
Runtime beats 67.38 % of python submissions.

"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                p1 = i + j
                p2 = i + j + 1
                result = mul + pos[p2]
                pos[p1] += result / 10
                pos[p2] = result % 10
        number = ""
        print ('pos', pos)
        for p in pos:
            if not (len(number) == 0 and p == 0):
                number += str(p)
        if not number:
            return "0"
        return number