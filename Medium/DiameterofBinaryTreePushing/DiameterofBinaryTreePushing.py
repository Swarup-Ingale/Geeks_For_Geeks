''' Structure of binary tree Node 
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def diameter(self, root):
        self.max_diameter = 0
        
        def depth(node) -> int:
            if not node:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            return 1 + max(left_depth, right_depth)
        
        depth(root)
        return self.max_diameter