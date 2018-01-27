class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        """
         * There're 3 possibilities to satisfy one edit distance apart: 
         * 
         * 1) Replace 1 char:
              s: a B c
              t: a D c
         * 2) Delete 1 char from s: 
              s: a D  b c
              t: a    b c
         * 3) Delete 1 char from t
              s: a   b c
              t: a D b c
              
              
         """
        
        for i in range(min(len(s), len(t))):
            if s[i] != t[i]:
                # if s has the same lenght as t, so the only possibility is replacing one char in s and t
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                # else if t is longer than s, the only possibility is deleting one char from t
                elif len(s) < len(t):
                    return s[i:] == t[i+1:]
                # else if s is longer that t, so the only possibility is deleting one char from s
                else:
                    return t[i:] == s[i+1:]
        # all previous chars are the same, the only possibility is deleting the end char in the longer one of s and t
        return abs(len(s) - len(t)) == 1
