class Solution:

    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        freq = [0] * (n + 2)
        for x in arr:
            if x <= n:
                freq[x] += 1

        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = 0
        running_prod = 1
        count_less_equal = 0

        for m in range(r + 1):
            count_less_equal += freq[m]

            if m >= l:
                remaining = n - count_less_equal
                current_ways = (running_prod * pow2[remaining]) % MOD
                ans = (ans + current_ways) % MOD

            ways_to_pick_m = (pow2[freq[m]] - 1) % MOD
            running_prod = (running_prod * ways_to_pick_m) % MOD

            if running_prod == 0:
                break

        return ans