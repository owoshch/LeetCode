import queue as q

class Solution:    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        prev_elements = set([])
        queue = q.Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            if k - node.val in prev_elements:
                return True
            prev_elements.add(node.val)
            for child in [node.left, node.right]:
                if child:
                    queue.put(child)
        return False
            
        