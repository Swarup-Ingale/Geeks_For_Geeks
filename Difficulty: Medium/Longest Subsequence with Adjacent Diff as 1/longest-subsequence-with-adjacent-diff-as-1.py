class Solution:
    def longestSubseq(self, arr):
        if not arr:
            return 0
        
        max_val = max(arr)
        dp = [0] * (max_val + 2)
        max_len = 0
        
        for x in arr:
            dp[x] = max(dp[x - 1], dp[x + 1]) + 1
            
            if dp[x] > max_len:
                max_len = dp[x]
                
        return max_len