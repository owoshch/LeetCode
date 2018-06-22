class Solution(object):
    def find_letter_combitations(self, digits, cur_string, result, letters):
        if len(digits) == 0:
            result.append(cur_string)
        else:
            for letter in letters[digits[0]]:
                self.find_letter_combitations(digits[1:], cur_string + letter, result, letters)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        letters = {"1": "", "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], 
                  "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                  "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        result = []
        self.find_letter_combitations(digits, "", result, letters)
        
        return result
        