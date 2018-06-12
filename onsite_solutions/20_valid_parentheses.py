"""
Valid parentheses assignment.
Solution with stack.
Runtime beats 99.85 % of python3 submissions
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for bracket in s:
            if bracket == "{" or bracket == "(" or bracket == "[":
                stack.append(bracket)
            elif bracket == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif bracket == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif bracket == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
        return not stack