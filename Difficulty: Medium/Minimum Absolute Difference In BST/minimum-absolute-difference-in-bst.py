'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''
        
class Solution:
    def absDiff(self, root):
        min_diff = float('inf')
        prev_val = -float('inf')
        
        stack = []
        curr = root
        
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                diff = curr.data - prev_val
                if diff < min_diff:
                    min_diff = diff

                prev_val = curr.data
                curr = curr.right

        return min_diff