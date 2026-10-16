class Solution:
    def countAlwaysFound(self, arr):
        n = len(arr)
        if n <= 1:
            return n

        right_min = [0] * n
        right_min[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], arr[i])

        count = 0
        left_max = -1

        for i in range(n):
            is_greater_than_left = (i == 0) or (arr[i] > left_max)

            is_less_than_right = (i == n - 1) or (arr[i] < right_min[i + 1])

            if is_greater_than_left and is_less_than_right:
                count += 1

            if arr[i] > left_max:
                left_max = arr[i]

        return count