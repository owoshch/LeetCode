"""
June 8, 2018
Runtime beats 95.86 % of python3 submissions.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def store_paths(self, string, root, paths):
        if not root.left and not root.right:
            paths.append(string + str(root.val))
        else:
            if root.left:
                self.store_paths(string + str(root.val) + '->', root.left, paths)
            if root.right:
                self.store_paths(string + str(root.val) + '->', root.right, paths)
        return paths
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        return self.store_paths("", root, [])