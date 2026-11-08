class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        low = 1
        high = n * min(s1, s2)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            scanned = (mid // s1) + (mid // s2)

            if scanned >= n:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans