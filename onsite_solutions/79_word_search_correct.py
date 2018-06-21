class Solution(object):    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.find_word(board, i, j, word):
                    return True
        return False

    def find_word(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >=len(board[0]) or word[0] != board[i][j]:
            return False
        temp = board[i][j]
        board[i][j] = "-1"
        result = self.find_word(board, i + 1, j, word[1:]) or self.find_word(board, i - 1, j, word[1:]) \
        or self.find_word(board, i, j + 1, word[1:]) or self.find_word(board, i, j - 1, word[1:])
        board[i][j] = temp
        return result