class Solution(object):
    
    def construct_tree(self, nums, left_index, right_index):
        if left_index > right_index:
            return
        mid = (left_index + right_index) // 2
        node = TreeNode(nums[mid])
        node.left = self.construct_tree(nums, left_index, mid - 1)
        node.right = self.construct_tree(nums, mid + 1, right_index)
        return node
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return
        root = self.construct_tree(nums, 0, len(nums) - 1)
        return root
        