"""
24 minutes
DFS-based solution with storing levels numbers in tuples
Correct. 218 ms.
The runtime beats 3.26 % of python submissions. 
Should be some bottleneck here. Probably it's the libraries import.
""" 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




import Queue as q
from collections import defaultdict

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        nodes_count = defaultdict(int)
        levels_sums = defaultdict(int)
        queue = q.Queue()
        queue.put((root, 0))
        while not queue.empty():
            node, level = queue.get()
            nodes_count[level] += 1
            levels_sums[level] += node.val
            for child in [node.left, node.right]:
                if child:
                    queue.put((child, level + 1))
        average_scores = []
        for _sum, _count in zip(levels_sums.values(), nodes_count.values()):
            average_scores.append(float(_sum) / _count)
        return average_scores