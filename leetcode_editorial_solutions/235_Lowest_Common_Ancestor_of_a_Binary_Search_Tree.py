class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        left_node, right_node = sorted([p.val, q.val])
        while not (left_node <= root.val <= right_node):
            root = (root.left, root.right)[root.val < left_node]
        return root