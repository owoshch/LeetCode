"""
Iterative solution for binary tree baths problem.
Runtime beats 19.05 % of python3 submissions.
(Because of queue lib import)
"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue as q
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        if not root:
            return []
        queue = q.Queue()
        queue.put((root, ""))
        while not queue.empty():
            node, string = queue.get()
            if not node.left and not node.right:
                paths.append(string + str(node.val))
            string += (str(node.val) + '->')
            if node.left:
                queue.put((node.left, string))
            if node.right:
                queue.put((node.right, string))
        return paths