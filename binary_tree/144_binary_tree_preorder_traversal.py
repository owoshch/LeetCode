class Solution(object):
    # recursively
    def preorderTraversal(self, root):
        result = []
        self.preOrder(root, result)
        return result
    def preOrder(self, root, result):
        if root:
            result.append(root.val)
            self.preOrder(root.left, result)
            self.preOrder(root.right, result)