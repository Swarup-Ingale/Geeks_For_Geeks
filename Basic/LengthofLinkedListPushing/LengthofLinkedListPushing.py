''' Structure of linked list Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def getCount(self, head):
        count = 1
        while head.next != None:
            count += 1
            head = head.next
            
        return count