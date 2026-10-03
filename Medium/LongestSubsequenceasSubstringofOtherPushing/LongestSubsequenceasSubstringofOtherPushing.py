class Solution:
    def longestMatch(self, a, b):
        n = len(a)
        m = len(b)
        max_len = 0
        
        for i in range(m):
            t = i
            for j in range(n):
                if t >= m:
                    break
                if a[j] == b[t]:
                    t += 1
                    
            max_len = max(max_len, t - i)
        
        return max_len