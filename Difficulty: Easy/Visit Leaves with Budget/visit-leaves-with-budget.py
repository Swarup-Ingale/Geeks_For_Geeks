''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getCount(self, root, k):
        if not root:
            return 0
            
        leaf_costs = []
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()
            if not node.left and not node.right:
                leaf_costs.append(level)
                
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
                
        leaf_costs.sort()
        count = 0
        for cost in leaf_costs:
            if k >= cost:
                k -= cost
                count += 1
            else:
                break
                
        return count