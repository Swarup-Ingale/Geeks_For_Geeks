class Solution:
    def countBT(self, h: int) -> int:
        if h == 0 or h == 1:
            return 1

        MOD = 10**9 + 7

        dp0 = 1 
        dp1 = 1 

        for i in range(2, h + 1):
            dp_current = (dp1 * ((dp1 + 2 * dp0) % MOD)) % MOD

            dp0 = dp1
            dp1 = dp_current

        return dp1