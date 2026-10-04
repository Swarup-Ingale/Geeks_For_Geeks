'''  Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        dummy = Node(0)
        curr = dummy
        
        while head1 and head2:
            if head1.data > head2.data:
                curr.next = head2
                head2 = head2.next
            else:
                curr.next = head1
                head1 = head1.next
            curr = curr.next
        
        if head1:
            curr.next = head1
        else:
            curr.next = head2
        
        return dummy.next