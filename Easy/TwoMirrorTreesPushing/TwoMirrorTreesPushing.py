''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:
    def areMirror(self, a, b):
        if not a and not b:
            return True
        
        if not a or not b:
            return False
        
        return (
            a.data == b.data and self.areMirror(a.left, b.right) and self.areMirror(a.right, b.left))