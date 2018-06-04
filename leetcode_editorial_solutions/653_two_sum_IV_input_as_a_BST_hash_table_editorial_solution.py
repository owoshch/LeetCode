class Solution:
    def find(self, root, k, prev_values):
        if not root:
            return False
        if k - root.val in prev_values:
            return True
        prev_values.add(root.val)
        return self.find(root.left, k, prev_values) or self.find(root.right, k, prev_values)
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        return self.find(root, k, set([]))