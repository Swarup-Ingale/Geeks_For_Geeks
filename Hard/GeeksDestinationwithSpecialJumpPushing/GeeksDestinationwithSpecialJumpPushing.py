class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int:
        MOD = 1_000_000_007
        m = a - b

        # Sum of ceil(u / m) for u = 1..n
        def sum_ceil(n: int) -> int:
            if n <= 0:
                return 0
            q, rem = divmod(n, m)
            return m * (q * (q + 1) // 2) + rem * (q + 1)

        L = d - r
        R = d - l
        cnt = R - L + 1

        # Part 1: sum of (x + 1) for x in [L, R]
        part1 = cnt * (L + R + 2) // 2

        # Part 2: 2 * b * sum of ceil((x - a) / m) for x in [max(L, a + 1), R]
        u2 = R - a
        u1 = max(L, a + 1) - a
        part2 = 0
        if u1 <= u2:
            part2 = 2 * b * (sum_ceil(u2) - sum_ceil(u1 - 1))

        return (part1 + part2) % MOD