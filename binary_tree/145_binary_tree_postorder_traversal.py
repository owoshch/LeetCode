# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.recursivePostOrder(root, result)
        return result
    def recursivePostOrder(self, root, result):
        if root:
            self.recursivePostOrder(root.left, result)
            self.recursivePostOrder(root.right, result)
            result.append(root.val)