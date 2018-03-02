class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root






        
        '''
        left_node, right_node = sorted([p.val, q.val])
        while not (left_node <= root.val <= right_node):
            root = (root.left, root.right)[root.val < left_node]
        return root
        '''