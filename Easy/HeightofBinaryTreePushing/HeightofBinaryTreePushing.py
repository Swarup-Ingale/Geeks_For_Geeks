''' Structure of Binary Tree Node
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        if not root:
            return -1
            
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        return 1 + max(left_height, right_height)