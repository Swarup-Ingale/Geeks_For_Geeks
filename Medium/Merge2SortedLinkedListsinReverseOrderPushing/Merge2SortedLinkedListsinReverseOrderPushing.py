'''Structure for linked list Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
'''
class Solution:
    def mergeResult(self, head1, head2):
        result_head = None
        
        curr1 = head1
        curr2 = head2
        
        while curr1 and curr2:
            if curr1.data <= curr2.data:
                next_node = curr1.next
                curr1.next = result_head
                result_head = curr1
                curr1 = next_node
            else:
                next_node = curr2.next
                curr2.next = result_head
                result_head = curr2
                curr2 = next_node

        while curr1:
            next_node = curr1.next
            curr1.next = result_head
            result_head = curr1
            curr1 = next_node

        while curr2:
            next_node = curr2.next
            curr2.next = result_head
            result_head = curr2
            curr2 = next_node
    
        return result_head