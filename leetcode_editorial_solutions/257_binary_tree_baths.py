class Solution(object):
    #dfs + stack
    def binaryTreePaths1(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, line = stack.pop()
            if not node.left and not node.right:
                res.append(line + str(node.val))
            if node.left:
                stack.append((node.left, line + str(node.val) + '->'))
            if node.right:
                stack.append((node.right, line + str(node.val) + '->'))
        return res


    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        print (str(root.val) + '->')
        return [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)] + \
             [str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)]