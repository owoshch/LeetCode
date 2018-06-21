"""
Time limit exceeded
"""



class Solution(object):
    def find_word(self, board, i, j, word):
        if len(word) == 0:
            self.answer = True
        else:
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]):
                temp = board[i][j]
                if board[i][j] == word[0]:
                    board[i][j] = -1
                    self.find_word(board, i + 1, j, word[1:])
                    self.find_word(board, i, j + 1, word[1:])
                    self.find_word(board, i, j - 1, word[1:])
                    self.find_word(board, i - 1, j, word[1:])
                    board[i][j] = temp
            
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.answer = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find_word(board, i, j, word)
                if self.answer:
                    return True
        return False