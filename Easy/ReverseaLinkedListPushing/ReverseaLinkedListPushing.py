""" Structure of Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            new = curr.next
            curr.next = prev
            prev = curr
            curr = new
        return prev