""" Structure of linked list Node
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        if not head:
            return None
        
        prev = None
        curr = head
        count = 0
        
        while curr and count < k:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1
            
        if curr:
            head.next = self.reverseKGroup(curr, k)
        
        return prev