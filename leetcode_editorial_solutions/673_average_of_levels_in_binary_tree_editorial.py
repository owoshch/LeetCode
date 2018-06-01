"""
Fastest solution on LeetCode. 70 ms

"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return res
        q = [root]
        res = []
        while q != []:
            new_q = []
            count = 0
            su = 0.0
            for node in q:
                count += 1
                su += node.val
                if node.left != None:
                    new_q.append(node.left)
                if node.right != None:
                    new_q.append(node.right)
            res.append(su/count)
            q = new_q
        return res
            
        