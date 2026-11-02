''' Structure of Binary Tree Node
class Node:
    def _init_(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def mirror(self, root):
        if not root:
            return None
            
        root.right, root.left = root.left, root.right
        
        self.mirror(root.left)
        self.mirror(root.right)
        
        return root