class Solution(object):
    def is_alphanumeric(self, character):
        return character.isalpha() or character.isdigit()
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        left and right indeces
        iterate while left < right
        if not an alphanumeric characters - move in correct direction
        '''
        left = 0
        right = len(s) - 1
        while left < right:
            while not self.is_alphanumeric(s[left]) and left < len(s) - 1:
                left += 1
            while not self.is_alphanumeric(s[right]) and right > 0:
                right -= 1
            if left >= right:
                return True
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True