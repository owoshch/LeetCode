"""
With a given hint to use a hash table.
8 minutes. Accepted.
Runtime beats 95.89 % of python3 submissions.
"""


class Solution:
    def find_target_with_hash(self, root, k, prev_values):
        if root:
            if k - root.val in prev_values:
                return True
            prev_values.add(root.val)
            if self.find_target_with_hash(root.left, k, prev_values):
                return True
            if self.find_target_with_hash(root.right, k, prev_values):
                return True
        return False
        
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        return self.find_target_with_hash(root, k, set([]))