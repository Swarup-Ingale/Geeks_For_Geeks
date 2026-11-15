class Solution:

    def subsequenceSum(self, s):
        MOD = 10**9 + 7
        n = len(s)
        
        digit_sum = sum(int(ch) for ch in s)
        multiplier = pow(2, n - 1, MOD)
        
        return (digit_sum * multiplier) % MOD