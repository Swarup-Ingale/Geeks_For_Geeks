class Solution:
    def formPyramid(self, arr):
        n = len(arr)
        total_sum = sum(arr)

        left = [0] * n
        left[0] = min(arr[0], 1)
        for i in range(1, n):
            left[i] = min(arr[i], left[i-1] + 1)

        right = [0] * n
        right[n-1] = min(arr[n-1], 1)
        for i in range(n-2, -1, -1):
            right[i] = min(arr[i], right[i+1] + 1)

        max_peak = 0
        for i in range(n):
            max_peak = max(max_peak, min(left[i], right[i]))

        return total_sum - (max_peak * max_peak)