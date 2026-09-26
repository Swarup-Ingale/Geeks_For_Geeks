class Solution:
    def minimumCost(self, x, s, m, l, cs, cm, cl):
        dp = [float('inf')] * (x + 1)
        dp[0] = 0
        
        for i in range(1, x + 1):
            c_s = dp[max(0, i - s)] + cs
            c_m = dp[max(0, i - m)] + cm
            c_l = dp[max(0, i - l)] + cl
            
            dp[i] = min(c_s, c_m, c_l)
            
        return dp[x]