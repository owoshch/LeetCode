#Accepted, beats 54.48 python solutions
#https://leetcode.com/problems/sum-of-left-leaves/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root, is_left=False):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if not root.left and not root.right and is_left:
                return root.val
            return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)
        return 0