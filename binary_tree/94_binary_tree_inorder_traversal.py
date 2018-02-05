# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.recursiveInOrder(root, result)
        return result
    def recursiveInOrder(self, root, result):
        if root:
            self.recursiveInOrder(root.left, result)
            result.append(root.val)
            self.recursiveInOrder(root.right, result)