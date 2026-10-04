""" Structure of Linked List Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def getKthFromLast(self, head, k):
        slow = fast = head
        for _ in range(k):
            if not fast:
                return -1
            fast = fast.next
        if not fast:
            return slow.data
            
        while fast:
            slow = slow.next
            fast = fast.next

        return slow.data