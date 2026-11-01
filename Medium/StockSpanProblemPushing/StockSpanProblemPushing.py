class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        spans = [0] * n
        
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
                
            if not stack:
                spans[i] = i + 1
                
            else:
                spans[i] = i - stack[-1]
                
            stack.append(i)
        
        return spans