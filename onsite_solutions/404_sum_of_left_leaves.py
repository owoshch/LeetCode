#Accepted, beats 54.48 python solutions
#https://leetcode.com/problems/sum-of-left-leaves/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_leaves_sum = int(0)
        stack = []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    left_leaves_sum += int(node.left.val)
                else:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return left_leaves_sum