"""
26 minutes
DFS-based solution
Fails in the case of the tree with sequence of incomplete layers:
________0
_______/
______1
_____/
____5
""" 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import Queue as q

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level_sums = []
        level = 0
        nodes_count = 0
        cur_sum = 0
        queue = q.Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            nodes_count += 1
            cur_sum += node.val
            if nodes_count == 2 ** level:
                level_sums.append(float(cur_sum) / nodes_count)
                cur_sum = 0
                nodes_count = 0
                level += 1
            for child in [node.left, node.right]:
                if child:
                    queue.put(child)
        if nodes_count > 0:
            level_sums.append(float(cur_sum) / nodes_count)
        return level_sums