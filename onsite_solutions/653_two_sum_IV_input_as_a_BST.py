# 26 minutes, doesn't work
# fails in the case:
# ___2
#___/_\
#__1___3
# sum to find: 4, correct answer: True (1 + 3)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_node(self, root, k):
        if root:
            if root.val == k:
                return True
            elif root.val < k :
                return self.find_node(root.right, k)
            else:
                return self.find_node(root.left, k)
        return False
    
    
    def find_target_from_root(self, root, k):
        if root:
            residual = k - root.val
            print ('residual', residual)
            print ('k', k)
            if residual >= root.val:
                return self.find_node(root.right, residual)
            else:
                return self.find_node(root.left, residual)
        return False
    

    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        #print (self.find_target_from_root(root, k))
        if root:
            a = self.find_target_from_root(root, k)
            print ('a', a)
            b = self.find_target_from_root(root.left, k)
            print ('b', b)
            c = self.find_target_from_root(root.right, k)
            print ('c', c)
            return a or b or c
        return False
        