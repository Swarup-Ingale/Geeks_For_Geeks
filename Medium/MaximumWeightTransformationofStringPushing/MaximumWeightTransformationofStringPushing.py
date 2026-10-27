class Solution:
    def getMaxWeight(self, s):
        n = len(s)
        if n == 1:
            return 1

        dp2 = 0
        dp1 = 1

        for i in range(1, n):
            unpaired_weight = dp1 + 1

            pair_bonus = 4 if s[i] != s[i-1] else 3
            paired_weight = dp2 + pair_bonus

            current_max = max(unpaired_weight, paired_weight)

            dp2 = dp1
            dp1 = current_max

        return dp1