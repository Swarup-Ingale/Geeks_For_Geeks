class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        n = len(arr)

        if k == 0:
            return max(arr) - min(arr)

        if k == n - 1:
            return 0

        pref_min, pref_max = [0] * n, [0] * n
        suff_min, suff_max = [0] * n, [0] * n

        pref_min[0] = pref_max[0] = arr[0]
        for i in range(1, n):
            pref_min[i] = min(pref_min[i - 1], arr[i])
            pref_max[i] = max(pref_max[i - 1], arr[i])

        suff_min[n - 1] = suff_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], arr[i])
            suff_max[i] = max(suff_max[i + 1], arr[i])

        ans = float('inf')

        for i in range(n - k + 1):
            curr_min = float('inf')
            curr_max = float('-inf')

            if i > 0:
                curr_min = min(curr_min, pref_min[i - 1])
                curr_max = max(curr_max, pref_max[i - 1])

            if i + k < n:
                curr_min = min(curr_min, suff_min[i + k])
                curr_max = max(curr_max, suff_max[i + k])

            ans = min(ans, curr_max - curr_min)

        return ans