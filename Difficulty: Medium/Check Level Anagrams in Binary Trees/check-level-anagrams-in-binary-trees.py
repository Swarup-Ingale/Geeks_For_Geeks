"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""


class Solution:

    def areAnagrams(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        q1 = [root1]
        q2 = [root2]

        while q1 and q2:
            if len(q1) != len(q2):
                return False

            freq = {}

            for node in q1:
                freq[node.data] = freq.get(node.data, 0) + 1

            for node in q2:
                if node.data not in freq:
                    return False
                freq[node.data] -= 1
                if freq[node.data] == 0:
                    del freq[node.data]

            if freq:
                return False

            next_q1 = []
            for node in q1:
                if node.left:
                    next_q1.append(node.left)
                if node.right:
                    next_q1.append(node.right)
            q1 = next_q1

            next_q2 = []
            for node in q2:
                if node.left:
                    next_q2.append(node.left)
                if node.right:
                    next_q2.append(node.right)
            q2 = next_q2

        return not q1 and not q2