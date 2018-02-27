# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root, min_value=float('-inf'), max_value=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val <= min_value or root.val >= max_value:
            return False
        return self.isValidBST(root.left, min_value, root.val) and self.isValidBST(root.right, root.val, max_value)