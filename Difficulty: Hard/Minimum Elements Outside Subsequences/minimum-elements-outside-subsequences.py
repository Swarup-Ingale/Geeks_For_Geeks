class Solution:
    def minCount(self, arr):
        n = len(arr)
        dp = [[[-1] * 102 for _ in range(102)] for _ in range(n)]
        
        def solve(i: int, last_inc: int, last_dec: int) -> int:
            if i == n:
                return 0
                
            if dp[i][last_inc][last_dec] != -1:
                return dp[i][last_inc][last_dec]
                
            ans = solve(i + 1, last_inc, last_dec)
            
            if arr[i] > last_inc:
                ans = max(ans, 1 + solve(i + 1, arr[i], last_dec))
                
            if arr[i] < last_dec:
                ans = max(ans, 1 + solve(i + 1, last_inc, arr[i]))
                
            dp[i][last_inc][last_dec] = ans
            return ans
            
        max_included = solve(0, 0, 101)
        return n - max_included