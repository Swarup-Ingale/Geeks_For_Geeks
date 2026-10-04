''' Structure of Linked List Node
class Node:
    def __init__(self,val):
        self.next=None
        self.data=val
'''

class Solution:
    def removeLoop(self, head):
        if not head or not head.next:
            return
        slow = fast = head
        cycle = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                cycle = True
                break
            
        if not cycle:
            return
        
        slow = head
        if slow == fast:
            while fast.next != slow:
                fast = fast.next
            fast.next = None
            return
        
        while fast.next != slow.next:
            slow = slow.next
            fast = fast.next
        
        fast.next = None