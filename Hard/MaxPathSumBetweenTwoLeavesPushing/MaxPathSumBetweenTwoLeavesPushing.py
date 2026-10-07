'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:        
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return float('-inf')

            if not node.left and not node.right:
                return node.data

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            if node.left and node.right:
                self.max_sum = max(self.max_sum, left_sum + right_sum + node.data)
                return node.data + max(left_sum, right_sum)

            return node.data + left_sum if node.left else node.data + right_sum

        dfs(root)

        return self.max_sum if self.max_sum != float('-inf') else -1