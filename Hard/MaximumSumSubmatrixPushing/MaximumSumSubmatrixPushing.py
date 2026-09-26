class Solution:
    def maxRectSum(self, mat):
        n = len(mat)
        m = len(mat[0])
        max_sum = float('-inf')
        
        for top in range(n):
            temp = [0] * m
            
            for bottom in range(top, n):
                mat_bottom = mat[bottom]
                curr_max = 0
                max_now = float('-inf')
                
                for col in range(m):
                    temp[col] += mat_bottom[col]
                    
                    curr_max = max(temp[col], curr_max + temp[col])
                    if curr_max > max_now:
                        max_now = curr_max
                    
                if max_now > max_sum:
                    max_sum = max_now
                    
        return max_sum