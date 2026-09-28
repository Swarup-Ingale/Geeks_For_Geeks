class Solution:
    def canFillContainer(self, arr: list[int], k: int) -> bool:
        dp = [False] * (k + 1)
        dp[0] = True
        
        for i in arr:
            if i > k:
                continue
            
            for j in range(i, k + 1):
                if dp[j - i]:
                    dp[j] = True
                    
                
        return dp[k]