class Solution:  
    def in_order(self, root, values):
        if root:
            self.in_order(root.left, values)
            values.append(root.val)
            self.in_order(root.right, values)
        return values
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        elements = self.in_order(root, [])
        left_index = 0
        right_index = len(elements) - 1
        while left_index < right_index:
            cur_sum = elements[left_index] + elements[right_index]
            if k == cur_sum:
                return True
            elif k > cur_sum:
                left_index += 1
            else:
                right_index -= 1
        return False