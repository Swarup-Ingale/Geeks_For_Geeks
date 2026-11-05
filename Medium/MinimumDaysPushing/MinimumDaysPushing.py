class Solution:
    def getMinimumDays(self, s: str, p: list[int]) -> int:
        n = len(s)

        day_replaced = [0] * n
        for i in range(n):
            day_replaced[p[i]] = i + 1

        max_day_needed = 0

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                day_fixed = min(day_replaced[i], day_replaced[i + 1])
                max_day_needed = max(max_day_needed, day_fixed)

        return max_day_needed