# Editorial O(m^2 + n^2 + m * n) solution.
# Runtime beats 95.70 % of python3 submissions.

class Solution:
    def pre_order(self, root, left):
        if not root:
            if left:
                return "lnull"
            else:
                return "rnull"
        return "#" + str(root.val) + " " + str(self.pre_order(root.left, True)) + " " + str(self.pre_order(root.right, False))
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t or not s:
            return False
        s_values = self.pre_order(s, True)
        t_values = self.pre_order(t, True)
        try:
            return s_values.index(t_values) >= 0
        except ValueError:
            return False