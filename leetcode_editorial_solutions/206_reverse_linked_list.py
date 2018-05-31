# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_node = None
        while head:
            cur_node = head
            head = head.next
            cur_node.next = prev_node
            prev_node = cur_node
        return prev_node

"""
# recursive solution
class Solution(object):
    def _reverse(self, node, prev_node=None):
        if not node:
            return prev_node
        next_node = node.next
        node.next = prev_node
        return self._reverse(next_node, node)
    
    def reverseList(self, head):
        return self._reverse(head)
""" 