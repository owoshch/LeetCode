class Solution(object):
    # recursively
    def preorderTraversal(self, root):
        result = []
        self.preOrder(root, result)
        return result
    def preOrder(self, root, result):
        if root:
            result.append(root.val)
            self.preOrder(root.left, result)
            self.preOrder(root.right, result)

'''
# iteratively

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        result = []
        stack = [root]
        while stack:
            element = stack.pop()
            if element:
                result.append(element.val)
                stack.append(element.right)
                stack.append(element.left)
        return result


'''


