''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:
        stack1, stack2 = [], []
        curr1, curr2 = root1, root2
        res = []

        while (curr1 or stack1) and (curr2 or stack2):
            while curr1:
                stack1.append(curr1)
                curr1 = curr1.left

            while curr2:
                stack2.append(curr2)
                curr2 = curr2.left

            if not stack1 or not stack2:
                break

            top1 = stack1[-1]
            top2 = stack2[-1]

            if top1.data == top2.data:
                res.append(top1.data)
                stack1.pop()
                stack2.pop()
                curr1 = top1.right
                curr2 = top2.right
            elif top1.data < top2.data:
                stack1.pop()
                curr1 = top1.right
            else:
                stack2.pop()
                curr2 = top2.right

        return res