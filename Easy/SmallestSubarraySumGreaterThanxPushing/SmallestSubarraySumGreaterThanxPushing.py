class Solution:
    def smallestSubWithSum(self, arr, x):
        n = len(arr)
        curr_sum = 0
        min_len = n + 1
        left = 0

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > x:
                min_len = min(min_len, right - left + 1)
                curr_sum -= arr[left]
                left += 1

        return 0 if min_len == n + 1 else min_len