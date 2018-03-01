class Solution(object):   
    def depth(self, root):
        if not root:
            return 0
        L = self.depth(root.left)
        R = self.depth(root.right)
        self.ans = max(self.ans, L + R + 1)
        return 1 + max(L, R)
    
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        self.depth(root)
        return self.ans - 1